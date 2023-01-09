from api.mixins import FilterByUserQsMixin
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from ...permission import IsDeveloper, IsTeamManager, IsTeamManagerOrDeveloper
from api.common.finance.serializers import (
    ClientDetailSerializer,
    ClientUpdateSerializer,
    PartnerSerializer,
    PartnerDetailSerializer,
    ProjectSerializer,
    ProjectListSerializer,
    FinancialRequestDetailSerializer,
    FinancialRequestSerializer,
    PaymentAccountSerializer
)
from finance.models import (
    Client, 
    Partner,
    Project,
    FinancialRequest,
    PaymentAccount
)
from .filters import (
    ProjectFilter,
    FinancialRequestFilter,
)
import datetime

class ClientViewSet(FilterByUserQsMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    filter_backends = [SearchFilter, filters.OrderingFilter, DjangoFilterBackend ]
    search_fields=['full_name']
    ordering_fields=['full_name', 'company_name']

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            return ClientUpdateSerializer
        return ClientDetailSerializer


class PartnerViewSet(FilterByUserQsMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Partner.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST', 'PATCH']:
            return PartnerSerializer
        return PartnerDetailSerializer


class ProjectViewSet(FilterByUserQsMixin, viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method == 'GET' and self.action == 'list':
            return ProjectListSerializer
        else:
            return ProjectSerializer


class FinancialRequestViewSet(  FilterByUserQsMixin,
                                mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FinancialRequest.objects.all().order_by('-requested_at')
    filterset_class = FinancialRequestFilter
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['requested_at']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FinancialRequestDetailSerializer
        elif self.request.method in ['POST', 'PUT']:
            return FinancialRequestSerializer

    def create(self, request):
        serializer_data = request.data
        serializer_data['requester'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = FinancialRequestDetailSerializer(instance=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        kwargs['partial'] = True
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'request': request})
        serializer.is_valid(raise_exception=True)
        updated = serializer.update(instance, serializer.validated_data)
        formated = FinancialRequestDetailSerializer(updated)
        return Response(formated.data)


class PaymentAccountView(ListAPIView):
    serializer_class = PaymentAccountSerializer
    permission_classes = [IsTeamManagerOrDeveloper]
    queryset = PaymentAccount.objects.all()
