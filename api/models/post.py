from django.db import models
from .user import User


class Post(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        STATUS_DRAFT,
        STATUS_PUBLIC,
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        db_table = 'posts'
