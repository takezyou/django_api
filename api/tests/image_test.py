from django.urls import include, reverse
from django.conf.urls import url
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.urls import router as api
from api.models import User, Token, Image

import base64


class ImageCreateTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        url(r'api/v1/', include(api.urls))
    ]

    def setUp(self):
        """
        setUp for testing
        """
        self.BASE_DIR = '/app/api/'
        User.objects.create(username='user', email='user@test.com', profile='user', password='username')
        self.user = User.objects.get(username='user')
        self.token = Token.create(self.user)

    # 写真の保存
    def test_image_create_ok(self):
        url = reverse('image-list')
        # テストファイルのフルパス
        file_path = self.BASE_DIR + 'tests/test_images/200KB_test.jpg'
        # ファイル読み込み
        img = open(file_path, 'rb').read()
        # 画像をエンコードする
        img_base64 = base64.b64encode(img)

        data = {
            'image': img_base64,
        }
        # 写真を保存
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ファイルサイズエラー(1MB以上)
    def test_image_create_file_siza_error(self):
        url = reverse('image-list')
        # テストファイルのフルパス
        file_path = self.BASE_DIR + 'tests/test_images/1MB_test.JPG'
        # ファイル読み込み
        img = open(file_path, 'rb').read()
        # 画像をエンコードする
        img_base64 = base64.b64encode(img)

        data = {
            'image': img_base64,
        }
        # 写真を保存
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # stringではない時のエラー(strの文字列だったら全て許可してしまう)
    def test_image_create_base64_error(self):
        url = reverse('image-list')

        data = {
            'image': 1234,
        }
        # 写真を保存
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # authorizationのエラー
    def test_image_create_authorization_error(self):
        url = reverse('image-list')
        file_path = self.BASE_DIR + 'tests/test_images/200KB_test.jpg'
        img = open(file_path, 'rb').read()
        img_base64 = base64.b64encode(img)

        data = {
            'image': img_base64,
        }
        # 写真を保存
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # jsonがない時のエラー
    def test_image_create_json_error(self):
        url = reverse('image-list')
        file_path = self.BASE_DIR + 'tests/test_images/200KB_test.jpg'
        img = open(file_path, 'rb').read()
        img_base64 = base64.b64encode(img)

        # 写真を保存
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.token)
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # jsonが空の時のエラー
    def test_image_create_json_key_error(self):
        url = reverse('image-list')
        file_path = self.BASE_DIR + 'tests/test_images/200KB_test.jpg'
        img = open(file_path, 'rb').read()

        data = {
        }
        # 写真を保存
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.token)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

