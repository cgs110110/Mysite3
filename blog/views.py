from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    article=BlogArticle.objects.all()
    return render(request, 'base.html', {'article':article})

def show(request,article_id):
    article=BlogArticle.objects.get(id=article_id)
    body=article.body
    author=article.author
    pub=article.publish
    return render(request, 'blog/show.html', {'body':body, 'author':author, 'pub':pub})