# Generated by Django 4.2 on 2023-10-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_proba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.AddField(
            model_name='useritem',
            name='height',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
