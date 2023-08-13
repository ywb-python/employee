#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 21:20
# @Author  : ywb
# @Site    : 
# @File    : chart.py
# @Software: PyCharm
from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    """数据统计"""
    return render(request, 'chart_list.html')


def chart_bar(request):
    """构造柱状图的数据"""
    series = [
        {
            'name': '张三',
            'type': 'bar',
            'data': [5, 20, 36, 67, 56, 20, 60]
        },
        {
            'name': '李四',
            'type': 'bar',
            'data': [15, 24, 27, 45, 35, 34, 77]
        }
    ]
    legend_data = ['张三', '李四']
    x_axis_data = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
    result = {
        "status": True,
        "data": {
            "series": series,
            "legend_data": legend_data,
            "x_axis_data": x_axis_data,

        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """构造饼图的数据"""
    data = [
        {'value': 1048, 'name': 'it部门'},
        {'value': 735, 'name': '运营'},
        {'value': 580, 'name': '新媒体'},
        {'value': 484, 'name': '人力资源'},
        {'value': 300, 'name': '市场部'}
    ]
    result = {
        "status": True,
        "data": data
    }
    return JsonResponse(result)


def chart_line(request):
    """构造折线图的数据"""
    series = [{
        'name': '上海',
        'type': 'line',
        'stack': 'Total',
        'data': [120, 132, 101, 134, 90, 230, 210]
    },
    {
        'name': '深圳',
        'type': 'line',
        'stack': 'Total',
        'data': [220, 182, 191, 234, 290, 330, 310]
    },
    {
        'name': '重庆',
        'type': 'line',
        'stack': 'Total',
        'data': [150, 232, 201, 154, 190, 330, 410]
    }]
    legend_data = ['上海', '深圳', '重庆']
    x_axis_data = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
    result = {
        "status": True,
        "data": {
            "series": series,
            "legend_data": legend_data,
            "x_axis_data": x_axis_data,

        }
    }
    return JsonResponse(result)