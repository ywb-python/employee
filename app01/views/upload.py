#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 22:15
# @Author  : ywb
# @Site    : 
# @File    : upload.py
# @Software: PyCharm
import os

from django.http import HttpResponse
from django.shortcuts import render

from app01 import models
from app01.utils.form import UpForm, UpModelForm


def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')
    print(request.POST)
    # request.POST：获取用户提交的字符串数据
    # request.FILES：获取用户提交的所有文件

    file_object = request.FILES.get('avatar')
    print(file_object.name)
    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse(123)


def upload_form(request):
    title = "Form上传文件"
    if request.method == 'GET':
        form = UpForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        image_object = form.cleaned_data.get("img")
        media_file_path =  os.path.join("media", image_object.name)
        f = open(media_file_path, mode='wb')
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        models.Boss.objects.create(name=form.cleaned_data['name'],
                                   age = form.cleaned_data['age'],
                                   img=media_file_path)
        return HttpResponse("上传成功")
    return render(request, 'upload_form.html', {"form": form, "title": title})


def upload_model_form(request):
    title = "ModelForm上传文件"
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("上传成功")
    return render(request, 'upload_form.html', {"form": form, "title": title})
