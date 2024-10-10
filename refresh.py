#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bilibili_api import Credential, sync
from pprint import pprint

ct_dict = {
    'ac_time_value': 'xxx',
    'bili_jct': 'xxx',
    'buvid3': 'xxx',
    'dedeuserid': 'xxx',
    'sessdata': 'xxx'
}

credential = Credential(**ct_dict)
# print(sync(credential.check_refresh()))
sync(credential.refresh())
print("\n")
pprint(vars(credential))
