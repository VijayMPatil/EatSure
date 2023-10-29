from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser,models.Model):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email