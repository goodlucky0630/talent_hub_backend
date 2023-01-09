from django.urls import path

from .views import ApproveFinanicalRequestView, DeclineFinanicalRequestView


urlpatterns = [
    path('<int:pk>/approve/', ApproveFinanicalRequestView.as_view(), name='approve_financial_requests'),
    path('<int:pk>/decline/', DeclineFinanicalRequestView.as_view(), name='decline_financial_requests'),
]
