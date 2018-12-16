from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.contrib.auth.hashers import make_password
from api.urls import router as api
from api.models import User


class SignupTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    # ユーザー作成テスト
    def test_create_user_ok(self):
        url = reverse('signup-list')
        data = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, 'akita')
        self.assertEqual(User.objects.get().email, 'test@gmail.com')
        self.assertEqual(User.objects.get().profile, 'test')
        self.assertTrue(User.objects.get().check_password('akitakaito'))

    # profileはNoneでもよいのでテストしない
    # usernameが同じものがあるとエラー
    def test_create_user_username_error(self):
        url = reverse('signup-list')
        data = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        self.client.post(url, data, format='json')

        data = {
            'username': 'akita',
            'email': 'akita@gmail.com',
            'profile': 'akita',
            'password': 'akitakaito1',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # emailに同じものがあるとエラー
    # def test_create_user_email_error(self):
    #     pass

    '''
     passwordが8文字以下の場合はエラー
     passwordと他のusenameなどの類似度が高い場合エラー
     passwordが数字のみで構成せれていた場合エラー
    '''

    # def test_create_user_password_error(self):
    #     url = reverse('signup-list')
    #     data = {
    #         'username': 'akita',
    #         'email': 'test@gmail.com',
    #         'profile': 'test',
    #         'password': 'akita',  # 8文字以下にする
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


