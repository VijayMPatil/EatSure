from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from apps.user.views import UserRegistrationAPIView,LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", obtain_auth_token, name="login"),
    path("register/", UserRegistrationAPIView.as_view(), name="register"),
    path("logout/",LogoutAPIView.as_view() , name="logout_user"),
    
]