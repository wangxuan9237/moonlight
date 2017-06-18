# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm,RegisterForm,UserProfileForm,UserForm,UserInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile,UserInfo
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == "GET":
        loginform = LoginForm()
        return render(request,"account/login.html",{"loginform":loginform})
    elif request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            username = cd["username"]
            password = cd["password"]
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect("/blog")
            else:
                return HttpResponse("wrong username or password")
        else:
            return HttpResponse("invalid")

def user_logout(request):
    logout(request)
    return HttpResponse("success logout")

def user_register(request):
    if request.method == "GET":
        registerform = RegisterForm()
        userprofileform = UserProfileForm()
        return render(request,"account/register.html",{"registerform":registerform,"userprofileform":userprofileform})
    elif request.method == "POST":
        registerform = RegisterForm(request.POST)
        userprofileform = UserProfileForm(request.POST)
        if registerform.is_valid() and userprofileform.is_valid():
            new_user = registerform.save(commit=False)
            new_user.set_password(registerform.cleaned_data["password"])
            new_user.save()
            new_profile = userprofileform.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse("success add new user")
        else:
            return HttpResponse("sorry user add failed")

@login_required
def myself(request):
    user = User.objects.get(username = request.user.username)
    userprofile = UserProfile.objects.get(user = user)
    userinfo = UserInfo.objects.get(user = user)
    return render(request,"account/myself.html",{"user":user,"userprofile":userprofile,"userinfo":userinfo})

@login_required
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)
    if request.method == "POST":
        print "done"
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid()*userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            user.email = user_cd["email"]
            userprofile.birth = userprofile_cd["birth"]
            userprofile.phone = userprofile_cd["phone"]
            userinfo.school = userinfo_cd["school"]
            userinfo.company = userinfo_cd["company"]
            userinfo.profession = userinfo_cd["profession"]
            userinfo.address = userinfo_cd["address"]
            userinfo.aboutme = userinfo_cd["aboutme"]
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth":userprofile.birth,"phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school":userinfo.school,"company":userinfo.company,"profession":userinfo.profession,"address":userinfo.address,"aboutme":userinfo.aboutme})
        print "get"
        return render(request,"account/myself_edit.html",{"user_form":user_form,"userprofile_form":userprofile_form,"userinfo_form":userinfo_form})

@login_required
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request,"account/imagecrop.html")
