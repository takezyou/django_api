from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostListView(CommonView):

    # 投稿の一覧
    def list(self, request):
        # tokenの確認
        authorization = self.check_authorization()
        if authorization:
            # tokenがなかったり違っていたらJSONレスポンスを返す
            return authorization

        # 投稿のされている情報の取得(自分以外, 時系列順)
        post_lists = Post.list(self.token.user_id)

        # 取得したlistを1件づつ空のresultに保存し配列で返す
        result = []
        for post_list in post_lists:
            params = {'id': post_list.id, 'body': post_list.body, 'created_at': post_list.created_at}
            result.append(params)

        # safeをFalseにすることで配列を返せるようにしている
        return JsonResponse(result, safe=False, status=200)
