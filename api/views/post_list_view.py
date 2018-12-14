from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostListView(CommonView):
    def list(self, request):

        authorization = self.check_authorization()
        if authorization:
            return authorization

        post_lists = Post.list(self.token.user_id)

        result = []
        for post_list in post_lists:
            params = {'id': post_list.id, 'body': post_list.body, 'created_at': post_list.created_at}
            result.append(params)

        return JsonResponse(result, safe=False)
