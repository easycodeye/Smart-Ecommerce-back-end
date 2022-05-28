from django.db import models

# Create your models here.

class Main(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Photo(Main):
    path = models.ImageField('files/images')

class Description(Main):
    desc_ar = models.TextField()
    desc_en = models.TextField()