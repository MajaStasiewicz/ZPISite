# Generated by Django 4.2 on 2023-11-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_useritem_drawer_alter_useritem_hand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shredder',
        ),
        migrations.RemoveField(
            model_name='product',
            name='water',
        ),
        migrations.AddField(
            model_name='useritem',
            name='shredder',
            field=models.CharField(default='NISZCZARKA', max_length=20),
        ),
        migrations.AddField(
            model_name='useritem',
            name='water',
            field=models.CharField(default='DOZOWNIK', max_length=20),
        ),
    ]
