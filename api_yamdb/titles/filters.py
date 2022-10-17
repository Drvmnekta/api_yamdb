"""Module with filters for titles app."""

from django_filters import rest_framework as filters

from titles.models import Title


class TitleFilter(filters.FilterSet):
    """Title filter"""

    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        """Meta class for title filter."""
        
        model = Title
        fields = ['genre', 'category', 'name', 'year']
