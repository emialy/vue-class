from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = [
    ("male", "男"),
    ("female", "女"),
]

class User(AbstractUser):
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # gender = models.CharField(verbose_name="性别", max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(verbose_name="地址", max_length=100, default="")
    mobile = models.CharField(verbose_name="手机号", max_length=11, unique=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

