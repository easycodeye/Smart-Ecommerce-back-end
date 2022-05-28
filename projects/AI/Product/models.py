from django.db import models
from Utilitys.models import Main
from django.contrib.auth.models import User

# Create your models here.


class Product(Main):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    puyer = models.ManyToManyField(User, related_name='Puyer')
    seller = models.ManyToManyField(User, related_name='Seller')


class ProductType(Product):
    class ChoiseType(models.TextChoices):
        SIGLER = 'S'
        PLORUL = 'P'
    type = models.CharField(choices=ChoiseType.choices, max_length=10)
    count = models.FloatField()
