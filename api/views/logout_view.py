from django.http.response import JsonResponse
from rest_framework import viewsets
from api.models import User
from api.models import Token

from .common_view import CommonView


class LogoutView(CommonView):
    # ログアウト
    def create(self, request):
        # tokenの確認
        authorization = self.check_authorization()
        if authorization:
            # tokenがなかったり違っていたらJSONレスポンスを返す
            return authorization

        # ユーザーが存在するかの確認
        if not User.objects.filter(id=self.token.user_id).exists():
            # 存在しない場合は403を返却
            return JsonResponse({'message': 'User does not exist'}, status=403)

        # ユーザーの情報取得
        user = User.objects.get(id=self.token.user_id)

        # ログアウトがokならトークンをNoneにis_loginをFalseにする
        token = Token.logout(user)

        # ログアウトの結果をレスポンスで返す
        result = {
            'user_id': token.user_id,
            'is_login': token.is_login,
        }
        return JsonResponse(result, status=201)

