from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Image
import json


class ImageView(CommonView):

    def create(self, request):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

