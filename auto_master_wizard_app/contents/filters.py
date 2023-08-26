import django_filters
from auto_master_wizard_app.models import Content


class ContentsFilterSet(django_filters.FilterSet):

    content_type = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Content
        fields = []
