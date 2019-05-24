#coding=utf-8

import os, sys
import time
import datetime


def log_call_info(func):
    def wrapper(*args, **kargs):
        params = '{0} {1}'.format(args, kargs)
        print "enter function {func}, params:{params}".format(func=func.__name__, params=params)
        ret = func(*args, **kargs)
        print "leave function {func}".format(func=func.__name__, params=params)
        return ret
    return wrapper

@log_call_info
def test(a, b):
    print 'a={p1}, b={p2}'.format(p1=a, p2=b)
    pass

@log_call_info
def pack(*args):
    print locals()

@log_call_info
def packing(**kargs):
    print locals()


if __name__ == '__main__':
    test(1,2)
    test('qqq', b='333')

    pack(1, 'a', 2.3)
    packing(test=1, str1='a', fnum=2.3)
    

