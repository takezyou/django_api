# django_api


## 開発環境

```
言語
- Python 3.7
フレームワーク
- Django 2.1
- Django Rest Framework 3.9.0
```
### 起動方法
docker-composeを用いて開発環境を管理

```
# clone
$ git clone git@github.com:takezyou/django_api.git
or
$ git clone https://github.com/takezyou/django_api.git

$ cd django_api
# サービスのbuild
$ docker-compose build
# コンテナ起動
$ docker-compose up
```

下記にアクセス

```
http://0.0.0.0:8080/api/v1
```

### テスト方法
DjnagoのAPITestCaseを用いてテストを作成しています。  
circleciを用いた自動テストも導入しています。

```
$ docker-compose run web python manage.py test
```

## API仕様書

swaggerでapiの仕様を確認することができます。

```
http://0.0.0.0:8080/swagger-docs
```

## 参考文献
[Django](https://docs.djangoproject.com/ja/2.1/)  
[Djangoパスワード管理](https://code.i-harness.com/ja/docs/django~2.0/topics/auth/passwords)  
[Django REST framework カスタマイズ方法 - チュートリアルの補足](https://qiita.com/okoppe8/items/c58bb3faaf26c9e2f27f)  
[Django データベース操作 についてのまとめ](https://qiita.com/okoppe8/items/66a8747cf179a538355b)  

