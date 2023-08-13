#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 21:27
# @Author  : ywb
# @Site    : 
# @File    : order.py
# @Software: PyCharm
from datetime import datetime
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.form import OrderModelForm
from app01.utils.pagination import Pagination


def order_list(request):
    form = OrderModelForm()
    queryset = models.Order.objects.all().order_by("-id")
    page_object = Pagination(request, queryset)
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """新建订单(ajax请求)"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 自定义字段的值而不是通过用户输入
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(
            random.randint(1000, 9999))
        form.instance.admin_id = request.session['info']['id']
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


def order_delete(request):
    """删除订单(ajax请求)"""
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在"})
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    """获取订单详情"""
    uid = request.GET.get('uid')
    raw_dict = models.Order.objects.filter(id=uid).values("title",
                                                           'status',
                                                           "price").first()
    if not raw_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    result = {
        "status": True,
        "data": raw_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """编辑订单"""
    uid = request.GET.get('uid')
    print(request.GET)
    raw_object = models.Order.objects.filter(id=uid).first()
    if not raw_object:
        return JsonResponse({"status": False, "tips": "数据不存在,请刷新重试"})
    form = OrderModelForm(data=request.POST, instance=raw_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
