from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Q
from apps.location.models import Tower
from apps.user.models import CustomUser

# Create your models here.
PHONE_REGEX = '^[6-9][0-9]{9}$'

VENDOR_TYPE=(
    ('Indian','Indian'),
    ('Chinese','Chinese'),
    ('Mexican','Mexican'),
    ('Italian','Italian'),
    ('Thai','Thai'),
    ('Ukrainian','Ukrainian'),
    ('Continental','Continental'),
    ('South Indian','South Indian'),
    ('North Indian','North Indian'),
    ('Backery','Backery'),
    ('Juices','Juices'),
    ('Beverages','Beverages'),
    ('Sweets','Sweets'),
    ('Others','Others')

)

# def generate_unique_code(vendor_name):
#     name_split_array = vendor_name.split(" ")
#     if len(name_split_array) > 1:
#         unique_code = name_split_array[0][:2] + name_split_array[1][:2]
#     else:
#         unique_code=vendor_name[:4]
#     return unique_code.upper()    


class Vendor(models.Model):
    """ Create Vendor Model"""
    vendor_name = models.CharField(max_length=100,null=False,blank=False)
    vendor_phone = models.CharField(max_length=13,null=False,validators=[RegexValidator(
            regex=PHONE_REGEX,
            message='invalid number',
            code='invalid_phone')])
    vendor_email = models.EmailField(max_length=255,blank=True)
    #unique_code = models.CharField(max_length=10,blank=False,unique=True,editable=False)
    vendor_type = models.CharField(max_length=100,choices=VENDOR_TYPE,blank=True)
    display_image = models.ImageField(upload_to='images/display_images',blank=True)
    is_active = models.BooleanField(default=False)

    #def save(self,*args, **kwargs):
        # unique_code=self.unique_code
        # if not unique_code:
        #     unique_code=generate_unique_code(self.vendor_name)
        #     vendor_by_code = Vendor.objects.filter(Q(unique_code__startswith=unique_code))
        #     if len(vendor_by_code) > 1:
        #         self.unique_code = self.unique_code + str(len(vendor_by_code))
        #     else:
        #         self.unique_code = self.unique_code

        # super(Vendor,self).save(*args, **kwargs)        

    def __str__(self):
        return str(self.vendor_name)
    
    class Meta:
        """ verbose_name is a human-readable name for the field"""
        verbose_name = 'user'
        verbose_name_plural = 'vendor'
                  

class VendorLocation(models.Model):
    """Create a VendorLocation model for a given vendor"""
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)
    location = models.ForeignKey(Tower, on_delete=models.CASCADE,null=False,blank=False)
    users = models.ManyToManyField(CustomUser,blank=False,default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.vendor.vendor_name)+ '-'+str(self.location)
    
    class Meta:
        unique_together = (('vendor','location'))
        verbose_name = "Vendor Location"


class Category(models.Model):
    """ Create Category Model """
    category_name=models.CharField(max_length=100,null=False,blank=False)
    category_image= models.ImageField(upload_to='images/vendor',blank=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return str(self.category_name)
    
    class Meta:
        """verbose description"""
        verbose_name ='category'
        verbose_name_plural ='categories'


MENU_TYPE=(
    ('veg','VEG'),
    ('non-veg','NON-VEG')
)
class Menu(models.Model):
    """" Create Menu model"""
    menu_type=models.CharField(max_length=50,choices=MENU_TYPE,blank=False)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,blank=False)
    item_name= models.CharField(max_length=100,null=False,blank=False)
    item_image= models.ImageField(upload_to='image/vendor/menu',blank=True)
    description= models.CharField(max_length=500,default=None,blank=True)
    is_active= models.BooleanField(default=False)

    def __str__(self):
        return str(self.item_name)
    
    class Meta:
        """ verbose description"""
        verbose_name='menu'
        verbose_name_plural='menus'


class MenuLocation(models.Model):
    UNIT_TYPE = (('Plate','PLATE'),('pcs','PCS'),('Bottle','BOTTLE'))
    STATUS_TYPE = (('Inactive','Inactive'),('Active','Active'))
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,default=None,blank=False)
    vendor_location = models.ForeignKey(VendorLocation,null=False,blank=True,on_delete=models.CASCADE)
    price = models.FloatField(max_length=10, default=0.0)
    gst = models.FloatField(max_length=10, default=0.0)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=50,choices=UNIT_TYPE,default=None,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    special_info= models.CharField(max_length=100,choices=STATUS_TYPE,blank=True,null=True)

    def __str__(self):
        return  self.menu.item_name + " in "+ self.vendor_location.__str__()
    
    class Meta:
        """verbose description"""
        unique_together = (('menu', 'vendor_location'),)
        verbose_name = "menu in location"
        verbose_name_plural = "menus in location"







