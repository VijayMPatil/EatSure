from django.db import models
import uuid
from django.utils import timezone
from apps.user.models import CustomUser
# Create your models here.

class Wallet(models.Model):
    """Wallet model"""
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,primary_key=True)
    balance = models.FloatField(null=False,blank=False, default=0)
    last_recharge = models.FloatField(null=False,blank=False,default=0)

    class Meta:
        verbose_name = 'wallet'
        verbose_name_plural = 'wallets'


class Transaction(models.Model):
    """Create a transaction model"""
    TRANSACTION_MODE =(('Credit','Credit'),('Debit','Debit'),('UPI','UPI'))
    TRANSACTION_TYPE = (('Payment Gateway','Payment Gateway'),('Cash','Cash'),('Wallet','Wallet'))
    TRANSACTION_CATEGORY = (('Recharge','Recharge'),('Order','Order'))
    type = models.CharField(max_length=50,null=False,choices=TRANSACTION_TYPE)
    mode = models.CharField(max_length=50,null=False,choices=TRANSACTION_MODE)
    category = models.CharField(max_length=50,null=False,choices=TRANSACTION_CATEGORY)
    amount = models.FloatField(default=0.0,null=False)
    user = models.ForeignKey(CustomUser,blank=False,on_delete=models.CASCADE,default=None)
    timestamp = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name="employee",default=None)
    details = models.CharField(max_length=255,null=True,blank=True)
    collection_due = models.BooleanField(default=False)
    tax = models.FloatField(null=False,blank=False,default=0.0)
    success = models.BooleanField(default=False)

    class Meta:
        verbose_name='Transaction'
        verbose_name_plural='transactions'


class Collection(models.Model):
    """Create collection model"""
    amount = models.FloatField(null=False,blank=False,default=0.0)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE ,related_name='transactions',default=None)
    timestamp = models.DateTimeField(default=timezone.now)
    collected_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    note = models.CharField(max_length=255,null=True,blank=True)
    
    class Meta:
        verbose_name = 'collection'
        verbose_name_plural ='collections'

class Payment(models.Model):
    """Create payment model"""
    PAYMENT_STATUS=(
        ('Successful', 'Successful'),
        ('Failed','Failed'),
        ('Refunded','Refunded'),
        ('Partial','Partial'),
        ('Initial Refunded','Initial Refunded'),
        ('Initiated','Initiated'))
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=False)
    total = models.FloatField(null=False,blank=False,default=0.0)
    total_tax = models.FloatField(null=False,blank=False,default=0.0)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=70,choices=PAYMENT_STATUS)
    transactions = models.ManyToManyField(Transaction)
    payment_ref_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    note = models.CharField(max_length=255,default=None,blank=True,null=True)
    payment_response_id = models.CharField(max_length=255,default=None,blank=True,null=True)

    class Meta:
        verbose_name="payment"
        verbose_name_plural="payments"

