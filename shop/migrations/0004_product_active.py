# Generated by Django 3.1.2 on 2020-10-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201015_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]