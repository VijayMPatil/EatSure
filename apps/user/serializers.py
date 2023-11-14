from rest_framework import serializers
from .models import CustomUser,UserLocation
from apps.location.models import City, Company, Tower
from apps.location.serializers import CitySerializer,CompanySerializer,TowerSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name','last_name','phone','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does not match"})
        
        if CustomUser.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exist"})
        
        account = CustomUser(email=self.validated_data['email'],
                             first_name=self.validated_data['first_name'],
                             last_name=self.validated_data['last_name'],
                             phone=self.validated_data['phone'])# username=self.validated_data['username']
        account.set_password(password)
        account.save()
        return account


class UserLocationCreateSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        city = City.objects.get(id=obj.location.city.id)
        serializer = CitySerializer(city).data
        return serializer

    company = serializers.SerializerMethodField()

    def get_company(self, obj):
        company = Company.objects.get(id=obj.location.company.id)
        serializer = CompanySerializer(company).data
        return serializer

    tower = serializers.SerializerMethodField()

    def get_tower(self, obj):
        tower = Tower.objects.get(id=obj.location.id)
        serializer =TowerSerializer(tower).data
        return serializer

    class Meta:
        model = UserLocation
        fields = ('user', 'location', 'city', 'company', 'tower')
        read_only_fields = ('user',)
    

class UserLocationUpdateSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        city = City.objects.get(id=obj.location.city.id)
        serializer = CitySerializer(city).data
        return serializer

    company = serializers.SerializerMethodField()

    def get_company(self, obj):
        company = Company.objects.get(id=obj.location.company.id)
        serializer = CompanySerializer(company).data
        return serializer

    tower = serializers.SerializerMethodField()

    def get_tower(self, obj):
        tower = Tower.objects.get(id=obj.location.id)
        serializer = TowerSerializer(tower).data
        return serializer

    class Meta:
        model = UserLocation
        fields = ('user', 'location', 'city', 'company', 'tower')
        read_only_fields = ('user',)


class UserLocationSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        city = City.objects.get(id=obj.location.city.id)
        serializer = CitySerializer(city).data
        return serializer

    company = serializers.SerializerMethodField()

    def get_company(self, obj):
        company = Company.objects.get(id=obj.location.company.id)
        serializer = CompanySerializer(company).data
        return serializer

    tower = serializers.SerializerMethodField()

    def get_tower(self, obj):
        tower = Tower.objects.get(id=obj.location.id)
        serializer = TowerSerializer(tower).data
        return serializer

    class Meta:
        model = UserLocation
        fields = ('user', 'location', 'city', 'company', 'tower')
        read_only_fields = ('user',)
