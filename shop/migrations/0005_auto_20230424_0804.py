# Generated by Django 2.2 on 2023-04-24 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_products_isavailable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='isavailable',
            new_name='available',
        ),
    ]
