from rest_framework import generics
from .serializers import ProductMiniSerializer,ProductSerializer
from .models import Product
from django.db.models import Q

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductMiniSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q',None)
        if query != None:
            return Product.objects.filter(name__icontains=query)
        return Product.objects.all()


class ProductDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class=ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self):
        return Product.objects.get(id=self.kwargs['id'])


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class=ProductMiniSerializer

    def get_queryset(self):
        return Product.objects.all()

