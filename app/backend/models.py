from django.db import models

# Create your models here.
class OCRResult(models.Model):
    identification_number = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=10,blank=True)
    date_of_issue = models.CharField(max_length=10,blank=True)
    date_of_expiry = models.CharField(max_length=10,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)