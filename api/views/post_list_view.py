from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostListView(CommonView):
    def list(self, request):
        pass