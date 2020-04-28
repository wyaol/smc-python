# -*- encoding: utf-8 -*-
"""
@File: exceptions
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/20 0020     wyao      1.0         None
"""


class JWTNotExistException(Exception):
    def __str__(self):
        return 'JWT 不存在'
