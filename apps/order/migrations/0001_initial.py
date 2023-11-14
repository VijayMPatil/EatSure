# Generated by Django 4.0 on 2023-11-01 09:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        ('vendor', '0003_vendorlocation_menulocation'),
        ('user', '0002_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.menu')),
            ],
            options={
                'verbose_name': 'menuorder',
                'verbose_name_plural': 'menuorders',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='images/qr_code')),
                ('order_status', models.CharField(choices=[('Processing', 'Processing'), ('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Unconfirmed', 'Unconfirmed'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered'), ('BarCode', 'BarCode')], max_length=50)),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_no', models.CharField(default='', editable=False, max_length=100)),
                ('total_price', models.FloatField(default=0.0)),
                ('details', models.CharField(blank=True, default=None, max_length=512, null=True)),
                ('menu_order', models.ManyToManyField(to='order.MenuOrder')),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to='user.customuser')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
                ('vendor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
