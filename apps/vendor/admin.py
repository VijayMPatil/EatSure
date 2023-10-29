from django.contrib import admin
from apps.vendor.models import Vendor,VendorLocation,Menu,MenuLocation,Category
# Register your models here.

admin.site.register(Vendor)
admin.site.register(VendorLocation)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(MenuLocation)
