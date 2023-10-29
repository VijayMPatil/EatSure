from django.db import models

# Create your models here.

class State(models.Model):
    """ Create State Table"""
    state_name= models.CharField(max_length=100,unique=True,null=False,blank=False)
    is_active= models.BooleanField(default=True)

    def __str__(self):
        return str(self.state_name)
    
    class Meta:
        verbose_name = "state"
        verbose_name_plural = "states"


class City(models.Model):
    """Create City model"""
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=False,blank=False)
    city_name = models.CharField(max_length=150,null=False,blank=False)

    def __str__(self):
        return str(self.city_name)
    
    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

class Company(models.Model): 
    """Company model"""
    company_name=models.CharField(max_length=100,unique=True, null=False,blank=False)
    is_active=models.BooleanField(default=True)
    cities=models.ManyToManyField(City,blank=False,default=None)

    def __str__(self):
        return str(self.company_name)
    
    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"


class Tower(models.Model):
    """Tower model"""
    tower_name = models.CharField(max_length=100,null=False,blank=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tower_name)
    
    class Meta:
        verbose_name = "tower"
        verbose_name_plural ="towers"

