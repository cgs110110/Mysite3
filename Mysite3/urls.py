from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index
urlpatterns = [
    # Examples:
    url(r'^$', 'blog.views.index', name='blog'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'(?P<article_id>\d)/$','blog.views.show',name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include('account.urls',namespace='account')),
    url(r'^pwd_reset/',include('password_reset.urls',namespace='pwd_reset',app_name='pwd_reset')),
    url(r'^article/',include('article.urls',namespace='article',app_name='article')),
]
