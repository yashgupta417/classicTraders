from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class=UserSerializer

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        return get_user_model().objects.all()

class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class=UserSerializer

    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def get_object(self):
        return get_user_model().objects.get(id=self.kwargs['id'])

    def get_queryset(self):
        return get_user_model().objects.all()

