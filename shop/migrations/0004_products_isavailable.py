# Generated by Django 2.2 on 2023-04-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20230423_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='isavailable',
            field=models.BooleanField(default=True),
        ),
    ]
