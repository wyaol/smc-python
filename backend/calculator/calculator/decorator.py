# -*- encoding: utf-8 -*-
"""
@File: decorator
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/20 0020     wyao      1.0         None
"""
from calculator import exceptions


def jwt_require(function):
    def decorate(*argv, **kwargs):
        request = argv[0]
        if not hasattr(request, 'jwt'):
            raise exceptions.JWTNotExistException()
        function(*argv, **kwargs)
    return decorate
