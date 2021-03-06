# Generated by Django 3.0.7 on 2021-06-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pdesc', models.TextField()),
                ('pprice', models.IntegerField()),
                ('premaining', models.IntegerField()),
                ('pcategory', models.CharField(max_length=30)),
                ('pcolour', models.CharField(max_length=20)),
                ('pcompany', models.CharField(max_length=20)),
                ('pimage', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
