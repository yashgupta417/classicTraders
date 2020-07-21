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
        return get_user_model().objects.get(user_id=self.kwargs['id'])

    def get_queryset(self):
        return get_user_model().objects.all()



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class LoginAPIView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.id,
        })
