from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView
from .serializers import VendorLocationSerializer, VendorSerializer, MenuLocationSerializer
from rest_framework.generics import get_object_or_404
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework import status,filters
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from apps.user.models import UserLocation, CustomUser
from apps.vendor.models import VendorLocation, Vendor,MenuLocation
from rest_framework.response import Response

# Create your views here.

class VendorListAPIView(ListAPIView):
    serializer_class= VendorLocationSerializer
    permission_classes=[IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_id= self.request.user.id
        user = get_object_or_404(CustomUser, id=user_id)
        user_loc = get_object_or_404(UserLocation, user_id=user.id)
        vendor_loc = user_loc.location

        vendor_list = VendorLocation.objects.filter(Q(location=vendor_loc) | Q(is_active=True))
        ser = self.get_serializer(vendor_list, many=True)
        return JsonResponse(ser.data, status=status.HTTP_200_OK,safe=False)

class VendorSearchAPIView(ListAPIView):
    serializer_class = VendorLocationSerializer
    permission_classes=[IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['vendor__vendor_name', 'location__tower_name', 'location__city__city_name',
                     'location__company__company_name']
    
    def get(self, request, *args, **kwargs):
        user_id= self.request.user.id
        user_loc=get_object_or_404(UserLocation,user_id=user_id)
        vendor_loc = user_loc.location
        queryset = VendorLocation.objects.filter(Q(location=vendor_loc) | Q(is_active=True))
        serializer= VendorLocationSerializer(queryset,many=True)
        return JsonResponse(serializer.data,safe=False)

class VendorDetailsAPIView(RetrieveAPIView):
    serializer_class= VendorSerializer
    def get(self,request,*args,**kwargs):
        vendor= Vendor.objects.get(id=self.kwargs['id'])
        serializer= VendorSerializer(vendor)
        return JsonResponse(serializer.data,safe=False)
    

class MenuListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class= MenuLocationSerializer
    
    def list(self, request, *args, **kwargs):
        user_id= self.request.user.id
        vendor_id= self.kwargs['id']
        menu_type= self.request.query_params.get('menu_type',None)
        user_location= UserLocation.objects.get(user_id=user_id)
        if self.request.query_params:
            if menu_type:
                all_items= MenuLocation.objects.filter(vendor_location__vendor_id=vendor_id,
                                                       vendor_location__location_id=user_location.location.id,
                                                        menu__menu_type=menu_type,is_active=True
                                                      )
                category_names=all_items.values_list('menu__category__category_name',flat=True).distinct()
                category_items = []
                for category in category_names:
                    items=all_items.filter(menu__category__category_name=category)
                    all_items_names= items.values_list('menu__item_name',flat=True).distinct()
                    ser= self.get_serializer(items,many=True).data
                    result = {"category_name": category, "no_items": len(items), "items_names": all_items_names,
                              "items": ser}
                    category_items.append(result)
                return Response(category_items,status=status.HTTP_200_OK)

            else:
                raise ValidationError({"message": {"menu_type": "menu_type not supplied"}})
        
        else:
            all_items = MenuLocation.objects.filter(vendor_location__vendor_id=vendor_id,
                                                    vendor_location__location_id=user_location.location.id,
                                                    is_active=True)
            category_names = all_items.values_list('menu__category__category_name', flat=True).distinct()
            category_items = []
            for category in category_names:
                items = all_items.filter(menu__category__category_name=category)
                all_items_names = items.values_list('menu__item_name', flat=True).distinct()
                ser = self.get_serializer(items, many=True).data
                result = {"category_name": category, "no_items": len(items), "items_names": all_items_names,
                          "items": ser}
                category_items.append(result)
            return Response(category_items, status=status.HTTP_200_OK)
              


class MenuSearchAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuLocationSerializer
    search_fields = ['menu__item_name', 'menu__category__category_name', 'menu__menu_type']
    