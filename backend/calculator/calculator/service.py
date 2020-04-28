# -*- encoding: utf-8 -*-
"""
@File: service
@Contact: 289672494@qq.com
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/4/20 0020     wyao      1.0         None
"""
from calculator import models, utils


def add_user(username, password):
    user = models.User(username=username, password=password)
    user.save()


def add_debt(username, debt):
    models.Debt(username=username, user_debt=debt)


def if_user_exist(username):
    res = models.User.objects.filter(username=username)
    return len(res) > 0


def if_user_right(username, password):
    res = models.User.objects.filter(username=username, password=password)
    return len(res) > 0


def update_user(username, **kwargs):
    models.User.objects.filter(username=username).update(**kwargs)


def get_user_info(username):
    res = {
        'username': username
    }
    res['token'] = utils.JWT().get_token(res)
    user = models.User.objects.get(username=username)
    res['id'] = user.user_id
    res['name'] = user.user_name
    res['email'] = user.user_email
    res['sex'] = user.user_sex
    try:
        debt = models.Debt.objects.get(username=username)
        res['debt'] = debt.user_debt
    except Exception:
        res['debt'] = 0
    return res


def get_users():
    users = models.User.objects.all()
    res = []
    for user in users:
        res.append({
            'username': user.username,
            'id': user.user_id,
            'name': user.user_name,
            'sex': user.user_sex,
            'email': user.user_email,
            'debt': 0,
            'register_time': user.user_register_time.strftime('%Y-%m-%d')
        })
    return res
