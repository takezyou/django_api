from rest_framework import viewsets
import django.db
from django.http.response import JsonResponse

from api.models import Token


class CommonView(viewsets.ViewSet):

    # 共通の初期値を設定
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token: Token = None
        self.JSON401 = JsonResponse({'message': 'Unauthorized'}, status=401)

    # authorization keyのチェック
    def check_authorization(self):
        try:
            token = 'Token '
            # METAにHTTP_AUTHORIZATIONがあるか確認
            if 'HTTP_AUTHORIZATION' in self.request.META:
                # HTTP_AUTHORIZATION'中身の代入
                authorization = self.request.META['HTTP_AUTHORIZATION']

                # 'Token 'があるか判定
                if authorization.startswith(token):
                    # 受けっとたtokenの代入
                    authorization = authorization[len(token):]
                    # 受け取ったtokenでデータベースからtokenの情報取得して代入
                    self.token = Token.objects.get(token=authorization)
                    return
            # HTTP_AUTHORIZATION'がなかった時に401エラー
            return self.JSON401

        except:
            # 認証に失敗したら401エラーを返却
            return self.JSON401

