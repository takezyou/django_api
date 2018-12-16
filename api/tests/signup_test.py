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
    def test_create_account(self):
        url = reverse('signup-list')
        print(url)
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
