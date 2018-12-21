from django.db import models
from .user import User
from django.utils import timezone


class Post(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 200字にしてモデルを作成
    body = models.CharField(max_length=200)
    # 公開と下書きのステータスを保存する
    status = models.CharField(default=STATUS_DRAFT, max_length=8)
    # 論理削除
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'posts'

    @staticmethod
    def create(body, status, user_id):
        # 今の時間
        date = timezone.now()

        # 新規登録
        post = Post.objects.create(user_id=user_id, body=body, status=status, created_at=date, updated_at=date)

        return post

    @staticmethod
    def update(body, status, body_id):
        # 今の時間
        date = timezone.now()

        # 更新
        post = Post.objects.get(id=body_id)
        post.body = body
        post.status = status
        post.update_at = date
        post.save()

        return post

    @staticmethod
    def delete(body_id):
        # 削除
        post = Post.objects.get(id=body_id)
        post.is_deleted = True
        post.save()

        return post

    @staticmethod
    def list(user_id):
        # ステータスがdraftのもの以外でuser_idが自分のものじゃなくて論理削除していないものを時間が最新の順場で取得
        post_list = Post.objects.exclude(status='draft').exclude(user_id=user_id).exclude(is_deleted=True).order_by('created_at').reverse().all()

        return post_list
