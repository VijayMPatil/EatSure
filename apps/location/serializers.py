from rest_framework import serializers
from apps.location.models import State,City,Company,Tower

class CitySerializer(serializers.ModelSerializer):
    """City Serializer."""
    state=serializers.CharField(source='state.state_name')
    class Meta:
        model=City
        fields=['id','city_name','state']

class StateSerializer(serializers.ModelSerializer):
    """State Serializer."""
    class Meta:
        model=State
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):
    """Company Serializer."""
    cities= CitySerializer(many=True)
    class Meta:
        model=Company
        fields=['id','company_name','cities']

class TowerSerializer(serializers.ModelSerializer):
    """Tower Serializer"""
    company=serializers.CharField(source='company.company_name')
    city=serializers.CharField(source='city.city_name')
    class Meta:
        model=Tower 
        fields=['id', 'tower_name', 'is_active', 'company', 'city']     