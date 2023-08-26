from rest_framework import serializers
from auto_master_wizard_app import models


class FeedVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = '__all__'

