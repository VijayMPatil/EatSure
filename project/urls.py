
from django.contrib import admin
from django.urls import path,include
# import apps.user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/user/', include('apps.user.urls'))
]
