class FilterByUserQsMixin:
    def get_queryset(self):
        return self.queryset.filter_by_user(self.request.user)
