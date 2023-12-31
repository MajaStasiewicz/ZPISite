# Generated by Django 4.2 on 2023-11-25 11:40

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_product_shredder_remove_product_water_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('100.00'), max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
