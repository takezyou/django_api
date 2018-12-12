from django.db import models
from .user import User
from django.utils import timezone

import hashlib


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40)
    access_datetime = models.DateTimeField()

    def __str__(self):
        dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
        return self.user.email + '(' + dt + ') - ' + self.token

    @staticmethod
    def create(user: User):
        # ユーザの既存のトークンを取得
        if Token.objects.filter(user=user).exists():
            # トークンが既に存在している場合は削除する
            Token.objects.get(user=user).delete()

        # トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
        dt = timezone.now()
        str = user.email + user.password + dt.strftime('%Y%m%d%H%M%S%f')
        hash = hashlib.sha1(str.encode('utf-8')).hexdigest()  # utf-8でエンコードしないとエラーになる

        # トークンをデータベースに追加
        token = Token.objects.create(
            user=user,
            token=hash,
            access_datetime=dt)

        return token
