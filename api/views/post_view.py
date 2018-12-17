from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostView(CommonView):

    def create(self, request):
        try:
            authorization = self.check_authorization()
            if authorization:
                return authorization
            data = json.loads(request.body)
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        body = data['body']
        # 文字数が140字以内の判定
        if len(body) > 140:
            return JsonResponse({'message': 'Must be 140 characters or less'}, status=403)

        post = Post.create(data, self.token.user_id)

        result = {
            'id': post.id,
            'body': post.body,
            'status': post.status,

        }

        return JsonResponse(result, status=201)

    def partial_update(self, request, pk=None):
        try:
            authorization = self.check_authorization()
            if authorization:
                return authorization
            data = json.loads(request.body)
            body_id = pk
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        body = data['body']
        # 文字数が140字以内の判定
        if len(body) > 140:
            return JsonResponse({'message': 'Must be 140 characters or less'}, status=403)
        post = Post.update(data, body_id)

        result = {
            'id': post.id,
            'body': post.body,
        }

        return JsonResponse(result)

    def destroy(self, request, pk=None):
        authorization = self.check_authorization()
        if authorization:
            return authorization
        body_id = pk

        post = Post.delete(body_id)

        result = {
            'id': post.id,
            'body': post.body,
            'is_deleted': post.is_deleted,
        }

        return JsonResponse(result)
