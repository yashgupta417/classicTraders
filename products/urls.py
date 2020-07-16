from django.conf.urls import url
from .views import ProductCreateAPIView,ProductDetailAPIView,ProductListAPIView

urlpatterns=[   url(r'^product/new/$',ProductCreateAPIView.as_view()),
                url(r'^products/$',ProductListAPIView.as_view()),
                url(r'^product/(?P<id>\w+)/$',ProductDetailAPIView.as_view())
]