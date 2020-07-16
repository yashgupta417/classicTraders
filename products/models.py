from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,blank=False,null=False)
    image=models.ImageField(upload_to='images/products/',null=True,blank=True)

    purchase_price=models.DecimalField(max_digits=10,decimal_places=2)
    purchase_unit=models.CharField(max_length=10)

    min_retail_price=models.DecimalField(max_digits=10,decimal_places=2)
    max_retail_price=models.DecimalField(max_digits=10,decimal_places=2)
    retail_unit=models.CharField(max_length=10)

    min_wholesale_price=models.DecimalField(max_digits=10,decimal_places=2)
    max_wholesale_price=models.DecimalField(max_digits=10,decimal_places=2)
    wholesale_unit=models.CharField(max_length=10)

    added_by=models.ForeignKey(get_user_model(),related_name='products_added',on_delete=models.CASCADE)
    added_on=models.IntegerField()

    last_updated_by=models.ForeignKey(get_user_model(),related_name='products_last_updated',on_delete=models.CASCADE)
    last_updated_on=models.IntegerField()

    def __str__(self):
        return self.name


