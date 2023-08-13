#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 18:01
# @Author  : ywb
# @Site    : 
# @File    : admin.py
# @Software: PyCharm
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm


def admin_list(request):
    """管理员列表"""

    data_dict = {}
    search_data = request.GET.get("params", "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    context = {"queryset": page_object.page_queryset,
               "page_string": page_object.html()}
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """添加管理员"""
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        # 保存到数据库
        form.save()
        return redirect("/admin/list")
    return render(request, 'change.html', {'form': form})


def admin_edit(request, nid):
    """编辑管理员"""
    raw_object = models.Admin.objects.filter(id=nid).first()
    if not raw_object:
        msg = "管理员信息不存在"
        return render(request, "error.html", {"msg": msg})

    title = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModelForm(instance=raw_object)
        return render(request, 'change.html', {"form": form, "title": title})
    # 更新到数据库
    form = AdminEditModelForm(data=request.POST, instance=raw_object)
    if form.is_valid():
        # 默认保存用户输入的值，额外添加用户输入以外的值
        # forms.instance.字段名=值
        form.save()
        return redirect("/admin/list")
    return render(request, 'change.html', {"form": form, "title": title})


def admin_delete(request, nid):
    """删除用户"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list")


def admin_reset(request, nid):
    """重置密码"""
    raw_object = models.Admin.objects.filter(id=nid).first()
    if not raw_object:
        msg = "管理员信息不存在"
        return render(request, "error.html", {"msg": msg})

    title = f"重置密码--{raw_object.name}"
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})
    # 更新到数据库
    form = AdminResetModelForm(data=request.POST, instance=raw_object)
    if form.is_valid():
        # 默认保存用户输入的值，额外添加用户输入以外的值
        # forms.instance.字段名=值
        form.save()
        return redirect("/admin/list")
    return render(request, 'change.html', {"form": form, "title": title})