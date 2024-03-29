# Generated by Django 5.0.1 on 2024-01-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('experience', models.IntegerField(max_length=50)),
                ('current_CTC', models.IntegerField(max_length=50)),
                ('present_CTC', models.IntegerField(max_length=50)),
                ('mailid', models.EmailField(max_length=50)),
            ],
        ),
    ]
