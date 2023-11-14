from django.db import models
from django.utils import timezone
# from apps.location.models import Tower

from apps.vendor.models import Menu,Vendor
from apps.user.models import CustomUser
from apps.payment.models import Payment


# Create your models here.
class MenuOrder(models.Model):
    menu= models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(null=False,blank=False,default=0)
    price= models.FloatField(null=False,blank=False)

    class Meta:
        verbose_name = "menuorder"
        verbose_name_plural="menuorders"
    
    def __str__(self):
        return str(self.menu.item_name) + "-"+ str(self.price) + "-" + str(self.quantity)
    

class Order(models.Model):
    """Create order model"""
    ORDER_STATUS=(
        ('Processing','Processing'),
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('Unconfirmed','Unconfirmed'),
        ('Accepted','Accepted'),
        ('Cancelled','Cancelled'),
        ('Delivered','Delivered'),
        ('BarCode','BarCode'))
    user = models.ForeignKey(CustomUser,default=None,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,default=None,on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='images/qr_code',null=True,blank=True)
    order_status = models.CharField(max_length=50,choices=ORDER_STATUS,null=False)
    time_stamp = models.DateTimeField(default=timezone.now)
    order_no = models.CharField(max_length=100,blank=False,editable=False,default='')
    total_price = models.FloatField(null=False,blank=False,default=0.0)
    menu_order =  models.ManyToManyField(MenuOrder, blank=False)
    payment = models.ForeignKey(Payment,blank=False,on_delete=models.CASCADE,default='')
    details = models.CharField(max_length=512,null=True,blank=True,default=None)
    modified_by = models.ForeignKey(CustomUser,blank=True, null=True, on_delete=models.CASCADE, related_name="modified_by",
                                    default=None)
    
    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return "Order No " + self.order_no
        
