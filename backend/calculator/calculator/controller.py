# -*- encoding: utf-8 -*-
"""
@File: controller
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/19 0019     wyao      1.0         None
"""
import copy
import requests
from calculator import utils, service, decorator


SUCCESS_CODE = 0
DATA_EXISTS_IN_DATABASE = 5
DATA_NOT_EXISTS_IN_DATABASE = 6
RESPONSE = {
    'code': SUCCESS_CODE,
    'msg': '',
    'data': {}
}


def calculate(c_id):
    html = requests.get('http://127.0.0.1:8080/encrypt?id=%s' % c_id)
    res = html.json()
    id = res['data']['id']
    context = res['data']['context']

    html = requests.get('http://127.0.0.1:8080/down_file?id=%s&name=%s' % (id, context))
    helib = utils.HElib(id)
    with open(helib.get_path(context), "wb") as code:
        code.write(html.content)
    helib.calculate()

    html = requests.post('http://127.0.0.1:8080/decrypt', data={
        'id': helib.id
    }, files={
        'file': open(helib.get_path(helib.res_file_name), 'rb')
    })
    res = html.json()
    return res['data']


def register(request):
    response = copy.deepcopy(RESPONSE)
    try:
        username = request.POST['username']
        password = request.POST['password']
        if service.if_user_exist(username):
            response['code'] = DATA_EXISTS_IN_DATABASE
            response['msg'] = '用户已存在'
        else:
            service.add_user(username, password)
            response['msg'] = '添加成功'
    except Exception as e:
        response['code'] = -1
        response['msg'] = str(e)
    finally:
        return utils.render_json_response(response)


def login(request):
    response = copy.deepcopy(RESPONSE)
    try:
        username = request.POST['username']
        password = request.POST['password']
        if not service.if_user_exist(username):
            response['code'] = DATA_NOT_EXISTS_IN_DATABASE
            response['msg'] = '用户不存在'
        else:
            if not service.if_user_right(username, password):
                response['code'] = -1
                response['msg'] = '密码错误'
            else:
                response['data'] = service.get_user_info(username)
    except Exception as e:
        response['code'] = -1
        response['msg'] = str(e)
    finally:
        return utils.render_json_response(response)


# @decorator.jwt_require
def check_user(request):
    response = copy.deepcopy(RESPONSE)
    try:
        user_id = request.POST['id']
        user_sex = request.POST['sex']
        user_email = request.POST['email']
        html = requests.get('http://127.0.0.1:8080/get_user?id=%s' % (user_id))
        res = html.json()
        if res['code'] != SUCCESS_CODE:
            response['code'] = -1
            response['msg'] = '身份校验失败'
        else:
            username = request.jwt['username']
            service.update_user(username, user_id=user_id, user_name=res['data']['name'], user_sex=user_sex, user_email=user_email)
            response['data'] = service.get_user_info(username)
    except Exception as e:
        response['code'] = -1
        response['msg'] = str(e)
    finally:
        return utils.render_json_response(response)


def get_user(request):
    response = copy.deepcopy(RESPONSE)
    try:
        username = request.jwt['username']
        response['data'] = service.get_user_info(username)
    except Exception as e:
        response['code'] = -1
        response['msg'] = str(e)
    finally:
        return utils.render_json_response(response)


def get_debt(request):
    response = copy.deepcopy(RESPONSE)
    try:
        username = request.jwt['username']
        user_info = service.get_user_info(username)
        debt = calculate(user_info['id'])
        service.add_debt(username, debt=debt)
    except Exception as e:
        response['code'] = -1
        response['msg'] = str(e)
    finally:
        return utils.render_json_response(response)


def get_users(request):
    response = copy.deepcopy(RESPONSE)
    try:
        users = service.get_users()
        response['data'] = users
    except Exception as e:
        response['code'] = -1
        response['msg'] = str(e)
    finally:
        return utils.render_json_response(response)