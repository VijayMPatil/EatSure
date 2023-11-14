from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from apps.location.serializers import CitySerializer,StateSerializer,CompanySerializer,TowerSerializer
from apps.location.models import City,Company,Tower
# Create your views here.

class CityListAPIView(generics.ListAPIView):
    """  Fetches all the cities. """
    serializer_class=CitySerializer

    def list(self, request, *args, **kwargs):
        queryset = City.objects.all().order_by('city_name')
        serializer= CitySerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CompanyListAPIView(generics.ListAPIView):
    """ Fetches all the companies according to the city id. """
    serializer_class= StateSerializer

    def list(self, request,*args, **kwargs):
        city_id=self.kwargs['id']
        get_object_or_404(City,id=city_id)
        company = Company.objects.filter(cities=city_id, is_active=True).order_by('company_name')
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class TowerListAPIView(generics.ListAPIView):
    """Create tower list view"""
    serializer_class = TowerSerializer

    def list(self, request, *args, **kwargs):
        company_id = self.kwargs['id']
        city_id = self.kwargs['cid']
        get_object_or_404(City, id=city_id)
        get_object_or_404(Company, id=company_id)
        tower = Tower.objects.filter(company_id=company_id, city_id=city_id, is_active=True).order_by('tower_name')
        serializer = TowerSerializer(tower, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)