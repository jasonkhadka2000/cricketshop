# Generated by Django 3.0.7 on 2021-06-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_psize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_firstname', models.CharField(default='', max_length=10)),
                ('order_lastname', models.CharField(default='', max_length=20)),
                ('order_username', models.CharField(default='', max_length=20)),
                ('order_id', models.IntegerField(default=0)),
                ('order_contact1', models.CharField(default='', max_length=20)),
                ('order_contact2', models.CharField(default='', max_length=20)),
                ('order_email', models.CharField(default='', max_length=20)),
                ('order_location', models.CharField(default='', max_length=30)),
                ('order_allorders', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
