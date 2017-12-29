from django.conf.urls import url,include
from .views import index

urlpatterns = [
    url(r'^$','blog.views.index',name='blog_title'),
]