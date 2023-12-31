# Generated by Django 4.0 on 2023-11-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('user', '0002_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.tower')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
    ]
