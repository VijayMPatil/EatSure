from django.urls import path
from apps.location.views import CityListAPIView,CompanyListAPIView,TowerListAPIView
from apps.user.views import UserLocationCreateAPIView, UserLocationUpdateAPIView, UserLocationRetrieveAPIView

urlpatterns = [
    path("city/list/", CityListAPIView.as_view(), name="city_list"),
    path("city/<int:id>/company/list/", CompanyListAPIView.as_view(), name="company_list"),
    path("company/<int:id>/city/<int:cid>/tower/list/", TowerListAPIView.as_view(), name="tower_list"),

    path('user_loc/create/', UserLocationCreateAPIView.as_view(), name='user-location-create'),
    path('user_loc/update/', UserLocationUpdateAPIView.as_view(), name='user-location-update'),
    path('user_loc/', UserLocationRetrieveAPIView.as_view(), name='user-location-retrieve'),
   
]