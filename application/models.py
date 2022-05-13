from django.db import models

# Create your models here.
class Customer(models.Model):
    custid = models.AutoField(null= False,unique=True, primary_key=True) 
    fname = models.CharField(max_length=20)  
    lname = models.CharField(max_length=20)  
    gender = models.CharField(max_length=20)  
    username = models.CharField(max_length=20)
    passowrd = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    zip = models.IntegerField(default=0)
    district = models.CharField(max_length=20)  
    province = models.CharField(max_length=20)

class Category(models.Model):
    catid = models.AutoField(null=False,unique=True,primary_key=True)
    catname = models.CharField(max_length=20) 

class Product(models.Model):
    proid = models.AutoField(null=False,unique=True,primary_key=True)
    proprice = models.IntegerField()
    proname = models.CharField(max_length=20)
    promodel = models.CharField(max_length=10)
    custid = models.ForeignKey(Customer,on_delete=models.RESTRICT)
    catid = models.ForeignKey(Category,on_delete=models.RESTRICT)

class Cart(models.Model):
    cartid = models.AutoField(null=False,unique=True,primary_key=True) 
    totalprice = models.IntegerField()  
    quantity = models.IntegerField() 
    proid = models.ForeignKey('Product',on_delete=models.RESTRICT)

class Payment(models.Model):
    payid = models.AutoField(null=False,unique=True, primary_key=True)  
    paytype = models.CharField(max_length=10)  
    cartid = models.ForeignKey(Cart, on_delete=models.RESTRICT)  

class Review(models.Model):
    reviewid = models.AutoField(null=False,unique=True, primary_key=True)
    reviewtext = models.CharField( max_length=50)
    custid = models.ForeignKey(Customer, on_delete=models.RESTRICT)  
    proid = models.ForeignKey(Product,on_delete=models.RESTRICT)

