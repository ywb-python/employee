#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 12:23
# @Author  : ywb
# @Site    : 
# @File    : form.py
# @Software: PyCharm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm
from app01.utils.encrypt import md5


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3, label="姓名")

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time',
                  'gender', 'department']

        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control",
        #                                    "placeholder": "姓名"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"})
        # }


class PrettyModelForm(BootStrapModelForm):
    # 验证方式一
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ]
    )

    class Meta:
        model = models.PrettyNum
        # __all__表示将model中的所有字段加载到这里
        fields = "__all__"
        # # 表示将fields中定义的字段加载到这里
        # fields = ["mobile", "level", 'price', "status"]
        # # 表示除了level字段以外的其他字段都被加载到这里
        # exclude = ["level"]

    # 验证方式二
    def clean_mobile(self):
        # 获取用户传入的数据
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    # 表示在修改页面显示手机号，但不能修改。直接删去该内容表示页面不显示手机号
    # mobile = forms.CharField(
    #     label="手机号",
    #     disabled=True
    # )
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ]
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "level", 'price', "status"]
        # fields = ["level", 'price', "status"]

    def clean_mobile(self):
        # 获取用户传入的数据
        txt_mobile = self.cleaned_data['mobile']
        # self.instance.pk表示获取当前手机号对应的id
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exclude(
            id=self.instance.pk).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        # render_value=True代表在确认密码错误时原本输入的密码不会被清空
        # widget=forms.PasswordInput(render_value=True),
        widget=forms.PasswordInput,

    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        # widgets = {"password": forms.PasswordInput(render_value=True)}

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != password:
            raise ValidationError("密码不一致！")
        return md5(confirm)


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username"]


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        # render_value=True表示密码明文显示
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]

    def clean_password(self):
        password = self.cleaned_data.get("password")
        exists = models.Admin.objects.filter(id=self.instance.pk,
                                             password=password).exists()
        if exists:
            raise ValidationError("不能与以前的密码一致")
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != password:
            raise ValidationError("密码不一致！")
        return md5(confirm)


class LoginForm(BootStrapForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput, required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput(
        render_value=True), required=True)
    code = forms.CharField(label="验证码", widget=forms.TextInput, required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


class TaskModelForm(BootStrapModelForm):

    # detail = forms.CharField(label="详细信息", widget=forms.TextInput)

    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea,
            "detail": forms.TextInput,

        }


class OrderModelForm(BootStrapModelForm):

    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["oid", "admin"]


class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = '__all__'


