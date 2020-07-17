from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model=Product
        fields='__all__'
        depth=1

class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta():
        model=Product
        exclude=['added_by','last_updated_by']