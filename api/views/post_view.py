from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostView(CommonView):

    def create(self, request):
        try:
            self.check_authorization()
            data = json.loads(request.body)
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        post = Post.create(data, self.token.user_id)

        result = {
            'id': post.id,
            'body': post.body,
            'status': post.status,

        }

        return JsonResponse(result)

    def partial_update(self, request, pk=None):

        try:
            self.check_authorization()
            data = json.loads(request.body)
            body_id = pk
            print(body_id)
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        post = Post.update(data, body_id)

        result = {
            'id': post.id,
            'body': post.body,
        }

        return JsonResponse(result)
