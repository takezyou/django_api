from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.urls import router as api
from api.models import Token, Post, User


class LogoutTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    def setUp(self):
        """
        setUp for testing
        """
        User.objects.create(username='user1', email='user1@test.com', profile='user1', password='username1')
        self.user1 = User.objects.get(username='user1')
        self.token1 = Token.create(self.user1)

    # logoutの成功
    def test_logout_ok(self):
        url = reverse('logout-list')

        # logoutする
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.token)
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # authorizationエラー
    def test_logout_authorization_error(self):
        url = reverse('logout-list')

        # logoutする
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)