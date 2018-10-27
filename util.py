# coding=utf-8

import random
import time


def make_random_array(length, min=0, max=None):
    return [random.randint(min, max or length) for i in range(length)]


def exec_speed(fn, **kwargs):
    start = time.time()
    fn(**kwargs)
    end = time.time()
    spend = end - start
    print(spend)
    return spend
