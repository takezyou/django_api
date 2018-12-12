# django_api


##  起動方法

```
# サービスのbuild
$ docker-compose build
# コンテナ起動
$ docker-compose up -d
```

下記にアクセス

```
http://0.0.0.0:8080/api/v1
```

## API仕様書

全てjson形式で送る

```
# signup
http://0.0.0.0:8080/api/v1/signup/

username: ユーザー名
email: mailアドレス
profile: 自己紹介(jsonで保存してprofileを作れるようにする)
password: パスワード 
```

```
# login
http://0.0.0.0:8080/api/v1/login/

email: mailアドレス
password: パスワード
```

## 参考文献
[Djangoパスワード管理](https://code.i-harness.com/ja/docs/django~2.0/topics/auth/passwords)