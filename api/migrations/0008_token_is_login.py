# Generated by Django 2.1.4 on 2018-12-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181214_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='is_login',
            field=models.BooleanField(default=True),
        ),
    ]
