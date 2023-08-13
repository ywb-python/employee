#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 21:03
# @Author  : ywb
# @Site    : 
# @File    : task.py
# @Software: PyCharm
import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.form import TaskModelForm
from app01.utils.pagination import Pagination


def task_list(request):
    """任务列表"""
    # 数据库获取所有任务
    queryset = models.Task.objects.all().order_by('-id')
    form = TaskModelForm()
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "form": form
    }
    return render(request, 'task_list.html', context)


@csrf_exempt
def task_ajax(request):
    """任务列表"""
    # 获取get请求参数
    print(request.GET)
    # 获取post请求参数
    print(request.POST)
    data_dict = {"status": True, "data": [11, 22, 33, 44]}
    json_string = json.dumps(data_dict)
    return HttpResponse(json_string)
    # django内部的序列化工具
    # return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))