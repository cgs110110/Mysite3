from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article_column/$',views.article_column,name='article_column'),
    url(r'^rename_column/$',views.rename_article_column,name='rename_column'),
    url(r'^del_column/$',views.del_article_column,name='del_column'),
]