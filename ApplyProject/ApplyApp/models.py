from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
# from cloudinary_storage.storage import RawMediaCloudinaryStorage
# from cloudinary.models import CloudinaryField
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    qualification=models.CharField()
    experience=models.IntegerField()
    current_CTC=models.IntegerField()
    expected_CTC=models.IntegerField(default=0)
    mailid=models.EmailField(max_length=50)
    phonenumber=models.CharField(max_length=50,default=0)
    resume=models.FileField("news",default=None,null=True)
    # resume = models.FileField(upload_to='news/file_save/', default=None,null=True, storage=RawMediaCloudinaryStorage())