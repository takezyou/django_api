from django.db import models
from django.core.files.base import ContentFile
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from .user import User
import uuid
import imghdr


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    # imageのリサイズを行う(使い方はpostの画像はmiddleにしてprofileの画像はthumbnailにするとか)
    big = ImageSpecField(source="origin",
                         processors=[ResizeToFill(1280, 1024)],
                         format='JPEG'
                         )

    thumbnail = ImageSpecField(source='origin',
                               processors=[ResizeToFill(250, 250)],
                               format="JPEG",
                               options={'quality': 60}
                               )

    middle = ImageSpecField(source='origin',
                            processors=[ResizeToFill(600, 400)],
                            format="JPEG",
                            options={'quality': 75}
                            )

    small = ImageSpecField(source='origin',
                           processors=[ResizeToFill(75, 75)],
                           format="JPEG",
                           options={'quality': 50}
                           )

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'images'

    @staticmethod
    def create(file, user_id):

        date = timezone.now()

        # 12文字で作成
        file_name = str(uuid.uuid4())[:12]

        extension = imghdr.what(file_name, file)
        # jpegの時jpgにする
        extension = "jpg" if extension == "jpeg" else extension
        # fileの名前を定義
        complete_file_name = "%s.%s" % (file_name, extension)
        # ImageFieldに保存するためのobject
        data = ContentFile(file, name=complete_file_name)

        image = Image.objects.create(user_id=user_id, created_at=date, updated_at=date)
        image.image.save(complete_file_name, data, save=True)
        # # レスポンスで返すために1件取得する
        # image_get = Image.objects.filter(user_id=user_id, image='images/' + complete_file_name)

        return image
