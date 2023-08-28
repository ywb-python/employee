#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 21:41
# @Author  : ywb
# @Site    : 
# @File    : account.py
# @Software: PyCharm
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.code import check_code
from app01.utils.form import LoginForm


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', '')
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            # 将错误信息显示在密码框下面
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        request.session['info'] = {"id": admin_object.id,
                                   "name": admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)

        return redirect("/admin/list")
    return render(request, 'login.html', {"form": form})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect("/login/")


def image_code(request):
    """生成图片验证码"""
    img, code_str = check_code()
    request.session['image_code'] = code_str
    # 设置图片验证码的超时时间
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, "png")
    return HttpResponse(stream.getvalue())
