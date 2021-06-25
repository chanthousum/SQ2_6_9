from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=100)
class Product(models.Model):
    productName = models.CharField(max_length=100)
    barcode=models.IntegerField()
    unitPrice=models.FloatField()
    sellPrice = models.FloatField()
    qty=models.IntegerField()
    photo=models.ImageField(upload_to="media/",null=True,blank=True)
    category=models.ForeignKey("Category",on_delete=models.CASCADE)
