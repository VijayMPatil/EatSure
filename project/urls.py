from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# import apps.user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/user/', include('apps.user.urls')),
    path('location/', include('apps.location.urls')),
    path('vendor/', include('apps.vendor.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
