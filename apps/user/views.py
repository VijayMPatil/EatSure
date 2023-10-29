from .serializers import UserRegisterSerializer
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.contrib.auth.models import Group

from rest_framework.generics import CreateAPIView
# Create your views here.

class UserRegistrationAPIView(CreateAPIView):
    """ user registration"""
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        print(serializer)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            group = Group.objects.filter(name__exact='Customer').first()
            user_db = CustomUser.objects.get(id=account.id)
            user_db.groups.add(group)
            data['response'] = 'Account has been created'
            # data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors
        return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)

class LogoutAPIView(CreateAPIView):
    """ Logout User"""
    permission_classes= [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return JsonResponse({"Message": "You are logged out"}, safe=False, status=status.HTTP_200_OK)

# @api_view(["POST",])
# @permission_classes([IsAuthenticated])
# def logout_user(request):
#     if request.method == "POST":
#         request.user.auth_token.delete()
#         return JsonResponse({"Message": "You are logged out"}, safe=False, status=status.HTTP_200_OK)        

    