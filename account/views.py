from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginForm,RegistrationForm,UserProfileForm
from .models import UserInfo,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfileForm,UserInfoForm
# Create your views here.

def user_login(request):
    if request.method=='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse('Welcome You. You have been authenticated successfully')

            else:
                return HttpResponse('Sorry,your username or password is not right')
        else:
            return HttpResponse('Invalid login')
    if request.method=='GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})

def register(request):
    if request.method=='POST':
        user_form = RegistrationForm(request.POST)
        userprofile_from=UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_from.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_from.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse('successfully')
        else:
            return HttpResponse('sorry you cant register')

    else:
        user_form = RegistrationForm()
        userprofile_from = UserProfileForm()
        return render(request,'account/register.html',{'form':user_form,'profile':userprofile_from})
@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,'account/myself.html',{'user':user,'userprofile':userprofile,'userinfo':userinfo})

@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method=='POST':
        user_from = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_from.is_valid() *userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_from.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.aboutme = userinfo_cd['aboutme']
            userinfo.address = userinfo_cd['address']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.school = userinfo_cd['school']
            user.save()
            userinfo.save()
            userprofile.save()
        return  HttpResponseRedirect('/account/my_information/')

    else:
        user_from = UserForm(instance=request.user)
        userprofile_form  = UserProfileForm(initial={'birth':userprofile.birth,'phone':userprofile.phone})
        userinfo_form = UserInfoForm(initial={'school':userinfo.school,'address':userinfo.address,'company':userinfo.company,'profession':userinfo.profession,'aboutme':userinfo.aboutme})
        return render(request,'account/myself_edit.html',{'user_form':user_from,'userprofile_form':userprofile_form,'userinfo_form':userinfo_form})
@login_required(login_url='/account/login/')
def my_image(request):
    if request.method=='POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request,'account/imagecrop.html',)