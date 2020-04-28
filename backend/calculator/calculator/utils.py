# -*- encoding: utf-8 -*-
"""
@File: utils
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/19 0019     wyao      1.0         None
"""
import json
import os
import jwt
from django.http import HttpResponse


def render_json_response(argv):
    return HttpResponse(json.dumps(argv, ensure_ascii=False), content_type="application/json,charset=utf-8")


class HElib:

    dir = '/home/files/calculator'
    calculate_tool_path = '/python/HElib/application/2x+y/build/2x+y'
    context_file_name = 'context.txt'
    res_file_name = 'result.txt'

    def __init__(self, id):
        self.id = id
        self.create_dir()

    def create_dir(self):
        c_dir = '%s/%s' % (self.dir, self.id)
        if not os.path.exists(c_dir):
            os.makedirs(c_dir)

    def calculate(self):
        os.system('%s %s %s' % (
            self.calculate_tool_path,
            self.get_path(self.context_file_name),
            self.get_path(self.res_file_name),
        ))

    def get_path(self, file_name):
        return '%s/%s/%s' % (self.dir, self.id, file_name)


class JWT:

    algorithm = 'HS256'
    secret_key = 'zhananbudanchou1234678'

    def get_token(self, play_load):
        return jwt.encode(
            play_load,  # payload, 有效载体
            self.secret_key,  # 进行加密签名的密钥
            algorithm=self.algorithm,  # 指明签名算法方式, 默认也是HS256
            headers={
                'alg': self.algorithm,  # 声明所使用的算法
            }  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
        ).decode('ascii')  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str

    def get_play_load(self, token):
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

