from django.db import models
from .user import User
from django.utils import timezone

import hashlib


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, null=True)
    # loginしていたら真
    is_login = models.BooleanField(default=True)
    access_datetime = models.DateTimeField()

    def __str__(self):
        dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
        return self.user.email + '(' + dt + ') - ' + self.token

    @staticmethod
    def create(user: User):
        # トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
        dt = timezone.now()
        str = user.email + user.password + dt.strftime('%Y%m%d%H%M%S%f')
        hash = hashlib.sha1(str.encode('utf-8')).hexdigest()  # utf-8でエンコードしないとエラーになる

        # ユーザの既存のトークンを取得
        if Token.objects.filter(user=user).exists():
            # ユーザーのトーク情報があったら新しくトークを追加してis_loginを1にする
            token = Token.objects.get(user=user)
            token.token = hash
            token.access_datetime = dt
            token.is_login = True
            token.save()

            return token

        # トークンをデータベースに追加
        token = Token.objects.create(
            user=user,
            token=hash,
            access_datetime=dt)

        return token

    @staticmethod
    def logout(user: User):
        token = Token.objects.get(user=user)
        token.token = None
        token.is_login = False
        token.save()

        return token
