import django_filters
from rest_framework import viewsets, filters

from api.serializers import PostSerializer
from api.models import Post


class PostView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        pass
