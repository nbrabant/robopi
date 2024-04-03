#!/usr/bin/env python3
from urllib.request import urlopen
import json

ROBO_URL = 'http://localhost:8888/'

def cal_api(url, data):
    data = json.dumps(data).encode()
    urlopen(url, data).read()

def call_robo(func, **args):
    cal_api(ROBO_URL + func, args)

call_robo('forward')
call_robo('backward')
call_robo('forward', duration=0.5, speed=1)
call_robo('backward', duration=0.5, speed=1)
call_robo('spin_right')
call_robo('spin_left')