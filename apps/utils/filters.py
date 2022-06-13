from django_filters import rest_framework as filters
from booktest.models import BookInfo

class BookFilter(filters.FilterSet):
    min_read = filters.NumberFilter(field_name='bread', lookup_expr='gte')
    max_read = filters.NumberFilter(field_name='bread', lookup_expr='lte')
    class Meta:
        model = BookInfo  #模型名
        fields = {
            'btitle': ['icontains'],
            'bcomment': ['gte', 'lte'],
        }