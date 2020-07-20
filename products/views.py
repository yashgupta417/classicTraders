from rest_framework import generics
from .serializers import ProductMiniSerializer,ProductSerializer
from .models import Product
from django.db.models import Q

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductMiniSerializer

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        query = self.request.query_params.get('q',None)
        if query != None:
            return Product.objects.filter(name__icontains=query)
        return Product.objects.all()


class ProductDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class=ProductSerializer

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self):
        return Product.objects.get(id=self.kwargs['id'])


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class=ProductSerializer

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        return Product.objects.all()

