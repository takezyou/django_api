from django.http.response import JsonResponse
from rest_framework import viewsets
from api.models import User
from api.models import Token

from .common_view import CommonView


class LogoutView(CommonView):

    def create(self, request):
        authorization = self.check_authorization()
        if authorization:
            return authorization

        if not User.objects.filter(id=self.token.user_id).exists():
            # 存在しない場合は403を返却
            return JsonResponse({'message': 'User does not exist'}, status=403)

        user = User.objects.get(id=self.token.user_id)
        # ログアウトがokならトークンをNoneにis_loginをFalseにする
        token = Token.logout(user)

        result = {
            'user_id': token.user_id,
            'is_login': token.is_login,
        }

        # トークンを返却
        return JsonResponse(result, status=201)

