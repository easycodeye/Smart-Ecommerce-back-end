from django.db import models

from Utilitys.models import Main
from django.contrib.auth.models import User
# Create your models here.


class BirthDate(Main):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()


class UserType(Main):
    class ChType(models.TextChoices):
        ADMIN = 'A'
        SELLER = 'S'
        BUYER = 'B'
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.TextField(choices=ChType.choices)
