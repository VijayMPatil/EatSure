from .serializers import UserRegisterSerializer
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.contrib.auth.models import Group

from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.user.models import UserLocation,CustomUser
from apps.user.serializers import UserLocationSerializer

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


class UserLocationCreateAPIView(CreateAPIView):
    """
    Creates the user location using the city id, company id, tower id provided in the body section.
    Bearer token Required.
    """
    permission_classes= [IsAuthenticated]
    serializer_class = UserLocationCreateSerializer

    def post(self, request, *args, **kwargs):
        # pass
        user_id= self.request.user.id
        user_loc= UserLocation.objects.filter(user_id=user_id)
        print(user_loc)
        if user_loc.first() ==None:
            serializer= self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=user_id)
                user= CustomUser.objects.get(id=user_id)
                user.user_loc_update=True
                user.save()
                return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
            else:
                errors=dict()
                for key in serializer.errors:
                    errors.__setitem__(key,serializer.errors[key][0].capitalize())
                    return JsonResponse({"message": errors},status=status.HTTP_400_BAD_REQUEST,safe=False)
        else:
            return JsonResponse({"message": 'Your location already exist'}, status=status.HTTP_409_CONFLICT, safe=False)        


class UserLocationUpdateAPIView(UpdateAPIView):
    """update user location information"""
    permission_classes=[IsAuthenticated]
    serializer_class = UserLocationUpdateSerializer

    def update(self, request, *args, **kwargs):
        user_id = self.request.user.id
        user_loc = UserLocation.objects.get(user_id=user_id)
        serializer = UserLocationUpdateSerializer(user_loc, data=request.data)
        if serializer.is_valid():
            serializer.save(**serializer.validated_data)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        errors = dict()
        for key in serializer.errors:
            errors.__setitem__(key, serializer.errors[key][0].capitalize())
        return JsonResponse({"message": errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLocationRetrieveAPIView(RetrieveAPIView):
    """
    Fetches the user location.
    Bearer token required.
    """
    permission_classes=[IsAuthenticated]
    serializer_class = UserLocationSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = self.request.user.id
        user_loc = get_object_or_404(UserLocation, user_id=user_id)
        return JsonResponse(self.get_serializer(user_loc).data, status=status.HTTP_200_OK)
