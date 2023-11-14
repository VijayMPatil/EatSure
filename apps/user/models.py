from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from apps.location.models import Tower
from django.core.validators import RegexValidator

name_REGEX = '^[a-zA-Z ]*$'

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)

class CustomUser(AbstractUser,models.Model):
    username = None
    name = models.CharField(max_length=30, blank=False,null=True, validators=[RegexValidator(
        regex=name_REGEX,
        message='name must be Alphabetic only',
        code='invalid_first_name'
    )])
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    user_loc_update= models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class UserLocation(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Tower, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email