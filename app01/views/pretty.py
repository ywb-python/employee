#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 12:27
# @Author  : ywb
# @Site    : 
# @File    : pretty.py
# @Software: PyCharm

from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import PrettyModelForm, PrettyEditModelForm
from app01.utils.pagination import Pagination


def pretty_list(request):
    """靓号列表"""
    # 按级别倒序排列

    # 搜索部分
    data_dict = {}
    search_data = request.GET.get("params", "")
    if search_data:
        data_dict["mobile__contains"] = search_data

    queryset = models.PrettyNum.objects.filter(**data_dict).order_by(
        "-level")
    page_object = Pagination(request, queryset=queryset)
    context = {"queryset": page_object.page_queryset,
               "search_data": search_data,
               "page_string": page_object.html()}
    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    """添加靓号"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        # 保存到数据库
        form.save()
        return redirect("/pretty/list")
    return render(request, 'pretty_add.html', {'form': form})


def pretty_edit(request, nid):
    """编辑靓号"""
    raw_object = models.PrettyNum.objects.filter(id=nid).first()
    if not raw_object:
        msg = "靓号信息不存在"
        return render(request, "error.html", {"msg": msg})
    if request.method == "GET":
        form = PrettyEditModelForm(instance=raw_object)
        return render(request, 'pretty_edit.html', {"form": form})
    # 更新到数据库
    form = PrettyEditModelForm(data=request.POST, instance=raw_object)
    if form.is_valid():
        # 默认保存用户输入的值，额外添加用户输入以外的值
        # forms.instance.字段名=值
        form.save()
        return redirect("/pretty/list")
    return render(request, 'pretty_edit.html', {'form': form})


def pretty_delete(request, nid):
    """删除用户"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty/list")

# Create your views here.
