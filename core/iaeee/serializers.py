from rest_framework import serializers
from iaeee.models import News


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description')
