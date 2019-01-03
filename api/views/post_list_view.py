from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostListView(CommonView):
    # 投稿の一覧
    def list(self, request):
        # tokenの確認
        if self.check_authorization():
            return self.check_authorization()

        # 投稿のされている情報の取得(自分以外, 時系列順)
        post_list = Post.list(self.token.user_id)

        # 取得したlistを1件づつ空のresultに保存し配列で返す
        result = [{'id': post.id, 'body': post.body, 'created_at': post.created_at} for post in post_list]

        # safeをFalseにすることで配列を返せるようにしている
        return JsonResponse(result, safe=False, status=200)
