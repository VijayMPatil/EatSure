from django.contrib import admin
from .models import CustomUser, UserLocation
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserLocation)
