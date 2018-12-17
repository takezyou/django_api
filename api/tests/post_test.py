from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.urls import router as api
from api.models import Token, Post


class PostCreateTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    # 投稿の成功
    def test_post_create_ok(self):
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

        data = {
           'body': 'test',
           'status': 'public',
        }
        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
