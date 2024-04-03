#!/usr/bin/env python3
from http.client import HTTPConnection
from statistics import mean, stdev
import json
import time

def cal_api(conn, url, data):
    body = json.dumps(data).encode()
    conn.request('POST', url, body)
    with conn.getresponse() as resp:
        resp.read()

def call_robo(conn, func, **args):
    return cal_api(conn, '/' + func, args)

def get_noop_timing(conn):
    start = time.perf_counter()
    call_robo(conn, 'noop')
    return (time.perf_counter() - start) * 1000

conn_initial = HTTPConnection('localhost:8888')
get_noop_timing(conn_initial)
conn = HTTPConnection('localhost:8888')
init = get_noop_timing(conn_initial)
stats = [get_noop_timing(conn) for i in range(100)]
print(' init:', init)
print('  max:', max(stats))
print('  avg:', mean(stats))
print('  min:', min(stats))
print('stdev:', stdev(stats))