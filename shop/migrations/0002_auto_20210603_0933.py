# Generated by Django 3.0.7 on 2021-06-03 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pcategory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pcolour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pcompany',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pimage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='premaining',
        ),
    ]
