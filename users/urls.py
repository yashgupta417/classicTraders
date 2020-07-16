from django.conf.urls import url
from .views import UserCreateAPIView,UserDetailAPIView

app_name='users'
urlpatterns=[   url(r'^signup/$',UserCreateAPIView.as_view()),
                url(r'^user/(?P<id>\w+)/$',UserDetailAPIView.as_view()),
            ]

from rest_framework.authtoken import views
urlpatterns += [
    url(r'^login$/', views.obtain_auth_token)
]