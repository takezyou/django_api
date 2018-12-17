from rest_framework import viewsets
import django.db
from django.http.response import JsonResponse

from api.models import Token


class CommonView(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token: Token = None

    # authorization keyのチェック
    def check_authorization(self):
        try:
            token = 'Token '
            if 'HTTP_AUTHORIZATION' in self.request.META:
                authorization = self.request.META['HTTP_AUTHORIZATION']
                if authorization.startswith(token):
                    authorization = authorization[len(token):]
                    self.token = Token.objects.get(token=authorization)
                    return
            return JsonResponse({'message': 'Unauthorized'}, status=401)

        except:
            # 認証に失敗したら401エラーを返却
            return JsonResponse({'message': 'Unauthorized'}, status=401)
