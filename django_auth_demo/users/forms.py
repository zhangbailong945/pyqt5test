#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   forms.py
@Time    :   2019/03/12 11:41:35
@Author  :   Loach 
@Version :   1.0
@Contact :   1207549344@qq.com
@License :   (C)Copyright 2017-2019, loachblog.com
@Desc    :   None
'''

# here put the import lib
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=User
        fields=("username","email")
