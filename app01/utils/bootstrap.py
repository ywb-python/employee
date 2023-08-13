#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 12:20
# @Author  : ywb
# @Site    : 
# @File    : bootstrap.py
# @Software: PyCharm
from django import forms


class BootStrap(object):

    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {"class": "form-control",
                                      "placeholder": field.label}


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass


