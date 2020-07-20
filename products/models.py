from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,blank=False,null=False)
    image=models.ImageField(upload_to='images/products/',null=True,blank=True)

    purchase_price=models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    purchase_unit=models.CharField(max_length=10,null=False,blank=False)

    min_retail_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    max_retail_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    retail_unit=models.CharField(max_length=10,null=True,blank=True)

    min_wholesale_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    max_wholesale_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    wholesale_unit=models.CharField(max_length=10)

    added_by=models.ForeignKey(get_user_model(),related_name='products_added',on_delete=models.CASCADE)
    added_on=models.IntegerField(null=True,blank=True)

    last_updated_by=models.ForeignKey(get_user_model(),related_name='products_last_updated',on_delete=models.CASCADE,null=True,blank=True)
    last_updated_on=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name


