# Generated by Django 3.0.7 on 2021-06-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210603_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='psize',
            field=models.CharField(default='', max_length=20),
        ),
    ]
