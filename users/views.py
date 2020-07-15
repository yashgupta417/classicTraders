from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class=UserSerializer
    def get_queryset(self):
        return get_user_model().objects.all()

class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class=UserSerializer
    def get_object(self):
        return get_user_model().objects.get(id=self.kwargs['id'])

    def get_queryset(self):
        return get_user_model().objects.all()

