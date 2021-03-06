# Generated by Django 3.2.8 on 2021-11-18 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=300, verbose_name='Address')),
                ('city', models.CharField(max_length=300, verbose_name='City')),
                ('postal_code', models.IntegerField(verbose_name='Postal Code')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date and time')),
                ('paid', models.BooleanField(default=False, verbose_name='Is paid')),
                ('delivery_status', models.CharField(choices=[('processing', 'Processing'), ('delivering', 'Delivering'), ('delivered', 'Delivered')], default='processing', max_length=10, verbose_name='Delivery status')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
