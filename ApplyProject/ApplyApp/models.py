from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    experience=models.IntegerField(max_length=50)
    current_CTC=models.IntegerField(max_length=50)
    present_CTC=models.IntegerField(max_length=50)
    mailid=models.EmailField(max_length=50)