from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.urls import router as api
from api.models import Token, Post

import random
import string


class PostCreateTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    # 投稿の成功(public)
    def test_post_create_ok(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 投稿下書き(draft)
    def test_post_create_draft_ok(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'draft',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # authorizationのエラー
    def test_post_create_authorization_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # jsonエラー
    def test_post_create_json_error(self):
        url_sigup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_sigup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # json keyエラー
    def test_post_create_json_key_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 投稿文が140字以上の時エラー
    def test_post_create_characters_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        # 140字以上のランダムな文字列作成
        body = ''.join(random.choices(string.ascii_letters + string.digits, k=141))

        data = {
            'body': body,
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostUpdateTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    # 投稿の修正
    def test_post_update_ok(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        data = {
            'body': 'akitakaito',
            'status': 'public'
        }
        # 投稿を修正
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.patch(url + url_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(Post.objects.get().body, 'test')

    # 下書きから公開にできるか
    def test_post_update_public_ok(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'draft',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        data = {
            'body': 'akitakaito',
            'status': 'public'
        }
        # 投稿を修正
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.patch(url + url_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(Post.objects.get().body, 'test')
        self.assertNotEqual(Post.objects.get().status, 'draft')

    # authorizationエラー
    def test_post_update_authorization_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        data = {
            'body': 'akitakaito',
            'status': 'public'
        }
        # 投稿を修正
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        response = self.client.patch(url + url_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # jsonがないエラー
    def test_post_update_json_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        # 投稿を修正
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.patch(url + url_id, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # json keyエラー
    def test_post_update_json_key_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 投稿文が140字以上の時エラー
    def test_post_update_characters_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        # 140字以上のランダムな文字列作成
        body = ''.join(random.choices(string.ascii_letters + string.digits, k=141))

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        data = {
            'body': body,
            'status': 'public'
        }
        # 投稿を修正
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.patch(url + url_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # body_idがなかった時のテストが必要


class PostDeleteTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    # 投稿の修正
    def test_post_delete_ok(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        # 投稿の論理削除
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.delete(url + url_id, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # authorizationのエラー
    def test_post_delete_authorization_error(self):
        url_signup = reverse('signup-list')
        url_login = reverse('login-list')
        url = reverse('post-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        # ユーザー作成
        self.client.post(url_signup, data_signup, format='json')

        data_login = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }
        # ログイン
        self.client.post(url_login, data_login, format='json')

        token = Token.objects.get().token

        data = {
            'body': 'test',
            'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.post(url, data, format='json')

        url_id = str(Post.objects.get().id) + '/'

        # 投稿の論理削除
        self.client.credentials(HTTP_AUTHORIZATION='Token ')
        response = self.client.delete(url + url_id, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
