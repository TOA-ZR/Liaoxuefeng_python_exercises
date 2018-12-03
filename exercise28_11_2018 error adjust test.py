#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" 错误，调试和测试"

__author__ = 'TOA Zhou'



#如果认为某段代码可能会出错，就可以用try来运行这段代码
try :
    print("try...")
    r = 10 / 0 #这里产生错误，则后续语句都不会被执行
    print("result : ",r)
#如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码
#即执行except语句块
except ZeroDivisionError as e:# 这是错误的一种
    #except BaseException as e: 这样写也可以，一网打尽所有错误
    print("except :",e) # e就是具体的错误名，这里是  division by zero
#执行完except之后，如果有finally语句块，则执行finally语句块。
#至此，执行完毕。
finally:
    print("finally...")
print("END")

try:
    print("try...")
    r = 10 / int("a")
    print("result : ",r)
except ValueError as e:
    print("ValueError :",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError :",e)
finally:
    print("finally...")
print("ENDDDDDD")

try:
    print("try...")
    r = 10 /int("2")
    print("result :",r)
except ValueError as e:
    print("ValueError :",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError :",e)
else:
    print("no error")
finally:
    print("finally...")
print("ENDnnn")

def bar(str):
    return 10/int(str)

def foo(str):
    return 2*bar(str)
try:
    foo()
except ValueError as e:
    print("ValueError")
except UnicodeError as e:
    print("UnicodeError")
except BaseException as e:
    print("BaseException : ",e)


def bar(str):
    return 10/int(str)


def foo(str):
    return 2*bar(str)

def main(str):
    try:
        foo(str)
    except Exception as e:
        print("Error :",e)
    finally:
        print("finally...")


#main("0")
"""
Error : division by zero
finally...
"""
#main("a")
"""
Error : invalid literal for int() with base 10: 'a'
finally...
"""

from functools import reduce

def str2num(s):
    return eval(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
   # print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    #print('99 + 88 + 7.6 =', r)

main()

def foo(s):
    n = int(s)
    #print(">>> n = %d" % n)
    return 10 / n

def main():
    foo("1")

main()

def foo(s):
    n = int(s)
    assert  n!= 0, "n is zero!"
    return 10/n

def main():
    foo("1")

main()

import logging
#logging.basicConfig(level=logging.ERROR) #要显示的级别


s = "1"
n = int(s)
logging.debug("Nnn = %d" %n)
logging.info("n = %d" %n)
#logging.warning("NN = %d" %n)
#logging.error("nNNNn  = %d" %n)

#print(10/n)

s = "1"
n = int(s)
#print(10/n)




