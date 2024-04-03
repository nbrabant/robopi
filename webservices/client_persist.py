#!/usr/bin/env python3
from http.client import HTTPConnection
import json

def cal_api(conn, url, data):
    body = json.dumps(data).encode()
    conn.request('POST', url, body)
    with conn.getresponse() as resp:
        resp.read()

def call_robo(conn, func, **args):
    return cal_api(conn, '/' + func, args)

conn = HTTPConnection('localhost:8888')
for speed in [1, 2, 3]:
    call_robo(conn, 'spin_right', speed=speed)
    call_robo(conn, 'spin_left', speed=speed)