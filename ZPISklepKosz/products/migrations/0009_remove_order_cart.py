# Generated by Django 4.2 on 2023-10-28 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]