from rest_framework import serializers
from apps.vendor.models import Vendor,VendorLocation,Category,Menu,MenuLocation
from apps.location.models import City,Company,Tower
from apps.location.serializers import CitySerializer,CompanySerializer,TowerSerializer
from project.settings import GST_INCLUDED_PRICE,GST_PERCENTAGE,MENU_QUANTITY_HIGHER_LIMIT,MENU_QUANTITY_LOWER_LIMIT

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'

class VendorIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields= ('id',)

class VendorLocationSerializer(serializers.ModelSerializer):
    vendor=VendorSerializer()
    city= serializers.SerializerMethodField('get_city')
    company= serializers.SerializerMethodField('get_company')
    tower= serializers.SerializerMethodField('get_tower')
    def get_city(self,obj):
        city=City.objects.get(id=obj.location.city.id)
        serializer=CitySerializer(city).data
        return serializer['city_name']
    

    def get_company(self,obj):
        company=Company.objects.get(id=obj.location.company.id)
        serializer=CompanySerializer(company).data
        return serializer['company_name']
    
    def get_tower(self,obj):
        tower=Tower.objects.get(id=obj.location.id)
        serializer=TowerSerializer(tower).data
        return serializer['tower_name']
    
    class Meta:
        model=VendorLocation
        fields=('vendor','location','is_active','city','company','tower')
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model= Menu
        fields='__all__'

class MenuIdSerializer(serializers.ModelSerializer):
    class Meta:
        model= Menu
        fields=('id',)


# pending
class MenuLocationSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    quantity_text = serializers.SerializerMethodField('get_quantity_text')
    inclusive_tax = serializers.SerializerMethodField('get_inclusive_tax')
    price = serializers.SerializerMethodField('get_price')
    gst = serializers.SerializerMethodField('get_gst')

    def get_price(self, obj):
        if GST_INCLUDED_PRICE:
            return obj.price + ((obj.price * obj.gst) / 100)
        else:
            return obj.price

    def get_gst(self, obj):
        if obj.gst:
            return ((obj.price * obj.gst) / 100)
        else:
            return 0

    def get_quantity_text(self, obj):
        if obj.quantity <= 0:
            return "unavailable"
        elif (obj.quantity > MENU_QUANTITY_LOWER_LIMIT) and (obj.quantity <= MENU_QUANTITY_HIGHER_LIMIT):
            if obj.unit:
                return "few " + str(obj.unit).lower()
            else:
                return "few quantity left"
        elif obj.quantity <= MENU_QUANTITY_LOWER_LIMIT:
            if obj.unit:
                return str(obj.quantity) + " " + str(obj.unit).lower() + " left"
            else:
                return str(obj.quantity) + " quantity left"

    def get_inclusive_tax(self, obj):
        return GST_INCLUDED_PRICE

    class Meta:
        model = MenuLocation
        fields = '__all__'
        
