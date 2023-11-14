# Generated by Django 4.0 on 2023-11-12 07:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_user_loc_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator(code='invalid_first_name', message='name must be Alphabetic only', regex='^[a-zA-Z ]*$')]),
        ),
    ]