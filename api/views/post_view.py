from .common_view import CommonView
from django.http.response import JsonResponse

from api.models import Post
import json


class PostView(CommonView):

    # 投稿
    def create(self, request):
        try:
            # tokenの確認
            if self.check_authorization():
                # tokenがなかったり違っていたらJSONレスポンスを返す
                return self.check_authorization()

            # JSONのデータの読み込み
            data = json.loads(request.body)

            # テキストの代入
            body = data['body']
            # statusの代入
            status = data['status']
        except:
            # JSONの読み込みに失敗 keyエラーでも失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        # 投稿(データベースに保存)
        post = Post.create(body, status, self.token.user_id)

        if isinstance(post, JsonResponse):
            return post
        else:
            # 結果をdictに保存しJSONレスポンスで返す
            result = {
                'id': post.id,
                'body': post.body,
                'status': post.status,

            }
            return JsonResponse(result, status=201)

    # 投稿の修正 下書きを公開
    def partial_update(self, request, pk=None):
        try:
            # tokenの確認
            authorization = self.check_authorization()
            if authorization:
                # tokenがなかったり違っていたらJSONレスポンスを返す
                return authorization

            # JSONのデータ読み込み
            data = json.loads(request.body)

            # テキストの代入
            body = data['body']
            # statusの代入
            status = data['status']
        except:
            # JSONの読み込みに失敗 keyエラーで失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        # 文字数が140字以内の判定
        if len(body) > 140:
            return JsonResponse({'message': 'Must be 140 characters or less'}, status=403)

        try:
            # 投稿の修正(データベースに更新)
            post = Post.update(body, status, body_id)

            # 結果をdictに保存しJSONレスポンスで返す
            result = {
                'id': post.id,
                'body': post.body,
                'post': post.status
            }
            return JsonResponse(result, status=200)
        except:
            return JsonResponse({'message': 'Dose not exist'}, status=400)

    # 投稿の削除
    def destroy(self, request, pk=None):
        # tokenの確認
        authorization = self.check_authorization()
        if authorization:
            # tokenがなかったり違っていたらJSONレスポンスを返す
            return authorization

        # pk(postのid)を代入
        body_id = pk

        # 投稿の削除(論理削除)
        post = Post.delete(body_id)

        # 結果をdictに保存しJSONレスポンスで返す
        result = {
            'id': post.id,
            'body': post.body,
            'is_deleted': post.is_deleted,
        }
        return JsonResponse(result)
