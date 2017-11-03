# coding=utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    post = request.POST
    name = post.get('user_name')
    pwd1 = post.get('pwd')
    pwd2 = post.get('cpwd')
    email = post.get('email')
    if pwd1 != pwd2:
        return redirect('/user/register/')
    else:
        # 加密
        s1 = sha1()
        s1.update(pwd1)
        pwd3 = s1.hexdigest()

        # 创建对象
        user = UserInfo()
        user.uname = name
        user.upwd = pwd3
        user.uemail = email
        user.save()
        # 注册成功，返回登录页
        return redirect('/user/login/')


def login(request):
    return render(request, 'df_user/login.html')