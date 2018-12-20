from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Image
import json
import six
import base64


class ImageView(CommonView):

    def create(self, request):
        try:
            authorization = self.check_authorization()
            if authorization:
                return authorization
            data = json.loads(request.body)
            # base64を受け取る
            image = data['image']
            # base64で受け取った値を変換してファイルとして保存できるようにする
            file = base64.b64decode(image)
            # base64の確認
            if not isinstance(image, six.string_types):
                return JsonResponse({'message': 'Does not base64'}, status=400)
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        # 作成
        Image.create(file, self.token.user_id)

        return JsonResponse({'result': 'ok'}, status=201)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

