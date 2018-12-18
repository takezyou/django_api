from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.utils import timezone
from api.urls import router as api
from api.models import Token, Post, User


class PostListTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    def setUp(self):
        """
        setUp for testing
        """
        User.objects.create(username='user1', email='user1@test.com', profile='user1', password='username1')
        User.objects.create(username='user2', email='user2@test.com', profile='user2', password='username2')
        self.user1 = User.objects.get(username='user1')
        self.token1 = Token.create(self.user1)
        self.user2 = User.objects.get(username='user2')
        self.token2 = Token.create(self.user2)

        date = timezone.now()
        # user1の投稿
        Post.objects.create(user_id=self.token1.user_id, body='test1', status='public', created_at=date, updated_at=date)
        Post.objects.create(user_id=self.token1.user_id, body='test2', status='public', created_at=date, updated_at=date)
        # user2の投稿
        Post.objects.create(user_id=self.token2.user_id, body='test3', status='public', created_at=date, updated_at=date)
        Post.objects.create(user_id=self.token2.user_id, body='test4', status='public', created_at=date, updated_at=date)

    # 投稿一覧
    def test_post_list_ok(self):
        url = reverse('post_list-list')

        # 投稿
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.token)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # authorizationエラー
    
