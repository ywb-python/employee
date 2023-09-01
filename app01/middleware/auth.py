#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 21:40
# @Author  : ywb
# @Site    : 
# @File    : auth.py
# @Software: PyCharm
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


# class M1(MiddlewareMixin):
#     """中间件1"""
#     def process_request(self, request):
#         """
#         如果该方法无返回值(默认返回None)，则继续向后执行
#         若有返回值，则不再向后执行
#         """
#         print("M1进来了")
#
#     def process_response(self, request, response):
#         print("M1,走了")
#         return response

#
# class M2(MiddlewareMixin):
#     """中间件2"""
#
#     def process_request(self, request):
#         print("M2进来了")
#
#     def process_response(self, request, response):
#         print("M2,走了")
#         return response


class AuthMiddleware(MiddlewareMixin):
    """中间件"""

    def process_request(self, request):
        if request.path_info in ["/login/", '/image/code/']:
            return
        info_dict = request.session.get("info")
        if info_dict:
            request.info_dict = info_dict
            return
        return redirect("/login/")

    def process_response(self, request, response):
        print("M2,走了")
        return response