# Generated by Django 5.0.1 on 2024-02-01 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='resume',
            field=models.FileField(default=None, null=True, upload_to='news/'),
        ),
    ]