from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.urls import router as api
from api.models import Token


class LoginTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    # ユーザーログインテスト
    def test_user_login_ok(self):
        url_sigup = reverse('signup-list')
        url = reverse('login-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        self.client.post(url_sigup, data_signup, format='json')

        # emailでログインする
        data = {
            'email': 'test@gmail.com',
            'password': 'akitakaito',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # jsonがない場合のエラー
    def test_user_login_json_error(self):
        url_sigup = reverse('signup-list')
        url = reverse('login-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        self.client.post(url_sigup, data_signup, format='json')

        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # usernameの場合のエラー
    def test_user_login_username_error(self):
        url_sigup = reverse('signup-list')
        url = reverse('login-list')

        data_signup = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        self.client.post(url_sigup, data_signup, format='json')

        data = {
            'username': 'akita',
            'password': 'akitakaito',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # emailが違う場合エラー
    def test_user_login_email_error(self):
        pass

