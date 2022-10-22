from rest_framework.filters import BaseFilterBackend
from django.db.models import Q


class ShowOnlyOwnOrSharedBudgets(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(Q(owner=request.user.id) | Q(shared=request.user.id)).distinct()
