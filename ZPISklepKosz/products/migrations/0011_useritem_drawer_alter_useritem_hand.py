# Generated by Django 4.2 on 2023-11-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_useritem_hand_useritem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritem',
            name='drawer',
            field=models.CharField(default='SZUFLADA', max_length=20),
        ),
        migrations.AlterField(
            model_name='useritem',
            name='hand',
            field=models.CharField(default='PRAWORECZNOSC', max_length=50),
        ),
    ]
