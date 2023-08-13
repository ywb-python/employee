#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/12 10:34
# @Author  : ywb
# @Site    : 
# @File    : city.py
# @Software: PyCharm
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import UpModelForm


def city_list(request):
    queryset = models.City.objects.all()
    return render(request, 'city_list.html', {'queryset': queryset})


def city_add(request):
    title = "新建城市"
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, 'upload_form.html',
                      {"form": form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/city/list/")
    return render(request, 'upload_form.html', {"form": form, "title": title})