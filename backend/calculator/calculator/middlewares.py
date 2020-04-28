# -*- encoding: utf-8 -*-
"""
@File: middlewares
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/20 0020     wyao      1.0         None
"""
from django.utils.deprecation import MiddlewareMixin
from calculator.utils import JWT


class JWTMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if 'Authorization' in request.headers.keys():
            token = request.headers['Authorization'].split(' ')[1]
            request.jwt = JWT().get_play_load(token)

    def process_response(self, request, response):
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Origin"] = "*"
        return response
