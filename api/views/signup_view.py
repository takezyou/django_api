from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError

from api.models import User
from .common_view import CommonView

import json


class SignUpView(CommonView):

    def create(self, request):
        try:
            # JSONの読み込み
            data = json.loads(request.body)
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        # Userの定義
        user = User.objects

        # JSONからusernameの取得
        username = data['username']

        # 同じusernameを持つ人が存在するか判定
        if user.filter(username=username).exists():
            return JsonResponse({'message': 'Duplicate entry username'}, status=400)

        # JSONからemailを取得
        email = data['email']

        # 同じemailが存在するか判定
        if user.filter(email=email).exists():
            return JsonResponse({'message': 'Duplicate entry email'}, status=400)

        try:
            # JSONからpasswordを取得
            password = data['password']

            # AUTH_PASSWORD_VALIDATORSで定義したルールにしたがってバリデーションを行う
            validate_password(password)

            # passwordをpbkdf2の形式に変換
            data['password'] = make_password(password)

            # dataをUserに渡しuserの作成を行う
            user = User.objects.create(**data)

            # 結果をJSON形式で返す
            result = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'profile': user.profile,
            }
            return JsonResponse(result, status=201)

        except ValidationError as e:
            # バリデーションにかかった時にerror messageと一緒にJSONレスポンスを返す
            return JsonResponse({'message': e.messages[0]}, status=403)
