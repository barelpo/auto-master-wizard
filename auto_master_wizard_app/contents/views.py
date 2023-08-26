from rest_framework.viewsets import ModelViewSet

from auto_master_wizard_app.contents.filters import ContentsFilterSet
from auto_master_wizard_app.contents.serializers import FeedVideoSerializer
from auto_master_wizard_app.models import Content


class ContentViewSet(ModelViewSet):

    serializer_class = FeedVideoSerializer
    queryset = Content.objects.all()
    filter_class = ContentsFilterSet
