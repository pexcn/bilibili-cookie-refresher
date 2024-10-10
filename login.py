#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bilibili_api import login, user, sync
from pprint import pprint

print("请登录：\n")
credential = login.login_with_qrcode_term()

try:
    credential.raise_for_no_bili_jct()
    credential.raise_for_no_sessdata()
except:
    print("登陆失败\n")
    exit()

# print("欢迎，", sync(user.get_self_info(credential))['name'], "!")
print("\n\n")

pprint(vars(credential))
