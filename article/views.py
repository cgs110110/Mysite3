from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import ArticleColumn
from django.contrib.auth.decorators import login_required
from .forms import ArticleColumnForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    if request.method=='GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        columns_form = ArticleColumnForm()
        return render(request,'article/column/article_column.html',{'columns':columns,'columns_form':columns_form})

    if request.method == 'POST':
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user,column=column_name)
            return HttpResponse('1')

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def rename_article_column(request):
    column_name = request.POST['column_name']
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse('1')
    except:
        return HttpResponse('0')

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')