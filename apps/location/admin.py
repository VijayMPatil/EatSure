from django.contrib import admin
from .models import City,State,Company,Tower

# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Tower)
