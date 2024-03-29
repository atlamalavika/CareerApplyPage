# Generated by Django 5.0.1 on 2024-02-02 07:10

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplyApp', '0004_alter_user_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.FileField(default=None, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='news/file_save/'),
        ),
    ]
