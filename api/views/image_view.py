from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Image
import base64
import json


class ImageView(CommonView):

    def create(self, request):
        try:
            authorization = self.check_authorization()
            if authorization:
                return authorization
            data = json.loads(request.body)
            image = data['image']
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        print(base64.b64decode(image))

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

