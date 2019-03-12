from django.db import models
#扩展User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    nickname=models.CharField(max_length=50,blank=True)
    email=models.EmailField(unique=True)

    class Meta(AbstractUser.Meta):
        pass