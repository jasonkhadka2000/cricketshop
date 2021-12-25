from django.db import models

# Create your models here.

class Product(models.Model):
    pname=models.CharField(max_length=100,default="")
    pdesc=models.TextField(default="")
    pprice=models.IntegerField(default=0)
    pcategory=models.CharField(max_length=30,default="")
    pcolour=models.CharField(max_length=20,default="")
    pcompany=models.CharField(max_length=20,default="")
    pimage=models.ImageField(upload_to="shop/images",default="")
    psize=models.CharField(max_length=20,default="")

    def __str__(self):
        return (self.pname)

class Order(models.Model):
    order_firstname=models.CharField(max_length=10,default="")
    order_lastname=models.CharField(max_length=20,default="")
    order_username=models.CharField(max_length=20,default="")
    order_id=models.IntegerField(default=0)
    order_contact1=models.CharField(max_length=20,default="")
    order_contact2=models.CharField(max_length=20,default="")
    order_email=models.CharField(max_length=20,default="")
    order_location=models.CharField(max_length=30,default="")
    order_allorders=models.CharField(max_length=200,default="")
    order_track=models.CharField(max_length=20,default="onprocess")


    def __str__(self):
        return (self.order_firstname)


