from django.db import models
from .user import User
from django.utils import timezone
from django.http.response import JsonResponse


class Post(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.CharField(max_length=200)
    status = models.CharField(default=STATUS_DRAFT, max_length=8)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        db_table = 'posts'

    @staticmethod
    def create(data, user_id):
        body = data['body']
        status = data['status']

        # 文字数が140字以内の判定
        if len(body) > 140:
            return JsonResponse({'message': 'Must be 140 characters or less'}, status=400)

        date = timezone.now()

        # 新規登録
        post = Post.objects.create(user_id=user_id, body=body, status=status, created_at=date, updated_at=date)

        return post

    @staticmethod
    def update(data, body_id):
        body = data['body']

        # 文字数が140字以内の判定
        if len(body) > 140:
            return JsonResponse({'message': 'Must be 140 characters or less'}, status=400)

        date = timezone.now()

        # 更新
        post = Post.objects.get(id=body_id)
        post.body = body
        post.update_at = date
        post.save()

        return post
