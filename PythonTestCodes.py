#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def log(msg):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print(msg + 'Fuck Yeah')
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@log('what is that ')
def Sum2(x, y):
    print(x, y)
    return x + y

Sum2(10 , 20)
a = 10
