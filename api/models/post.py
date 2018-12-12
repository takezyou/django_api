from django.db import models
from .user import User
from django.utils import timezone


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

        if len(body) > 140:
            return JsonResponse({'message': 'Must be 140 characters or less'}, status=400)

        date = timezone.now()

        post = Post.objects.create(user_id=user_id, body=body, status=status, created_at=date, updated_at=date)

        return post
