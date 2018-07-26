from iaeee.models import News
from iaeee.serializers import LeadSerializer
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = LeadSerializer
