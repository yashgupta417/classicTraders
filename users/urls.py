from django.conf.urls import url
from .views import UserCreateAPIView,UserDetailAPIView,LoginAPIView

app_name='users'
urlpatterns=[   url(r'^signup/$',UserCreateAPIView.as_view()),
                url(r'^user/(?P<id>\w+)/$',UserDetailAPIView.as_view()),
                url(r'^login/$',LoginAPIView.as_view()),
            ]

