#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 12:27
# @Author  : ywb
# @Site    : 
# @File    : user.py
# @Software: PyCharm
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import UserModelForm
from app01.utils.pagination import Pagination


def user_list(request):
    """用户列表"""
    queryset = models.UserInfo.objects.all()
    # for obj in query_list:
    #     print(obj.name, obj.age, obj.account,
    #           obj.create_time.strftime("%Y-%M-%d"), obj.gender)
    #     # 获取性别对应的汉字,对于有choices的字段，可以通过get_字段名_display()
    #     获取choices里面的实际内容
    #     print(obj.get_gender_display())
    #     print(obj.department_id)
    #     # 获取部门名称
    #     print(obj.department.title)
    page_object = Pagination(request, queryset, page_size=2)
    context = {"queryset": page_object.page_queryset,
               "page_string": page_object.html()}
    return render(request, 'user_list.html', context)


def user_add(request):
    """添加用户"""
    context = {"gender_choices": models.UserInfo.gender_choices,
               "depart_list": models.Department.objects.all()}
    if request.method == "GET":
        return render(request, 'user_add.html', context)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("account")
    create_time = request.POST.get("create_time")
    gender = request.POST.get("gender")
    department = request.POST.get("department")
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=create_time,
                                   gender=gender, department_id=department)
    return redirect("/user/list")


def user_model_form_add(request):
    """基于ModelForm添加用户"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 保存到数据库
        form.save()
        return redirect("/user/list")
    return render(request, 'user_model_form_add.html', {'form': form})


def user_delete(request, nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")


def user_edit(request, nid):
    """修改用户"""
    raw_object = models.UserInfo.objects.filter(id=nid).first()
    if not raw_object:
        msg = "用户信息不存在"
        return render(request, "error.html", {"msg": msg})
    if request.method == "GET":
        form = UserModelForm(instance=raw_object)
        return render(request, 'user_edit.html', {"form": form})
    # 更新到数据库
    form = UserModelForm(data=request.POST, instance=raw_object)
    if form.is_valid():
        # 默认保存用户输入的值，额外添加用户输入以外的值
        # forms.instance.字段名=值
        form.save()
        return redirect("/user/list")
    return render(request, 'user_edit.html', {'form': form})
