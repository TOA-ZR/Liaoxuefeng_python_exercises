#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" a test module "

__author__ = 'TOA Zhou'

import sys

def test():
    args =sys.argv
    if len(args)==1:
        print("Hello IPR")
    elif len(args)==2:
        print("Hello", args[:])
        print("Hello,%s" % args[1])
    else:
        print("too many arguments")

if __name__=='__main__':
    test()

def _private_1(name): #private
    return "hello, %s" % name

def _private_2(name): #private
    return "hi, %s" % name

def greeting(name): #public
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting("ZR"))
print(greeting("TOA Zhou"))
print(_private_1("asasas"))#没有方法阻止调用private函数或者变量，全凭使用习惯

'''
hi, ZR
hello, TOA Zhou
hello, asasas
'''
import test
print(test.__doc__)
# a test module


sys.path.append('/Users/michael/my_py_scripts')