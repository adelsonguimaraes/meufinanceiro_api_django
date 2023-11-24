from django_filters import rest_framework as filters
from transactions import models


class TransactionPortionFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name="due_date", lookup_expr='year__exact')
    month = filters.NumberFilter(field_name="due_date", lookup_expr='month__exact')
    date_range = filters.DateFromToRangeFilter(field_name='due_date', lookup_expr='lte')
    card_isnull = filters.BooleanFilter(field_name="transaction__credit_card", lookup_expr='isnull')
    transaction = filters.CharFilter(field_name="transaction__name", lookup_expr='icontains')
    created_range = filters.DateFromToRangeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = models.TransactionPortion
        fields = ['due_date']
