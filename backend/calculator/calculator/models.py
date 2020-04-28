# -*- encoding: utf-8 -*-
"""
@File: models
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/20 0020     wyao      1.0         None
"""
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    user_sex = models.SmallIntegerField(default=1)
    user_email = models.CharField(max_length=50)
    user_register_time = models.DateField(auto_now_add=True)


class Debt(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    user_debt = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)
