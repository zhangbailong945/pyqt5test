#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2019/03/12 12:14:34
@Author  :   Loach 
@Version :   1.0
@Contact :   1207549344@qq.com
@License :   (C)Copyright 2017-2019, loachblog.com
@Desc    :   None
'''

# here put the import lib
from django.urls import re_path
from . import views


app_name='users'

urlpatterns=[
    re_path(r'register/',views.register,name='register'),
]
