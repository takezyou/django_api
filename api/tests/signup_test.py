from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.contrib.auth.hashers import make_password
from api.models import User


class SignupTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/v1/', include('api.urls')),
    ]

    # ユーザー作成テスト
    def test_create_account(self):
        url = reverse('signup')
        data = {
            'username': 'akita',
            'email': 'test@gmail.com',
            'profile': 'test',
            'password': 'akitakaito',
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().name, 'akita')
        self.assertEqual(User.objects.get().email, 'test@gmail.com')
        self.assertEqual(User.objects.get().profile, 'test')
        self.assertEqual(User.objects.get().password, make_password('akitakaito'))
