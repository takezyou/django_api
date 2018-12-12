from django.http.response import JsonResponse
from rest_framework import viewsets
from api.models import User
from api.models import Token

import json


class LoginView(viewsets.ViewSet):

    def create(self, request, format=None):
        # リクエストボディのJSONを読み込み、メールアドレス、パスワードを取得
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        # メールアドレスからユーザを取得
        if not User.objects.filter(email=email).exists():
            # 存在しない場合は403を返却
            return JsonResponse({'message': 'The email is wrong.'}, status=403)

        user = User.objects.get(email=email)

        # パスワードチェック
        if not user.check_password(password):
            # チェックエラー
            return JsonResponse({'message': 'The password is incorrect'}, status=403)

        # ログインOKの場合は、トークンを生成
        token = Token.create(user)

        # トークンを返却
        return JsonResponse({'token': token.token})
