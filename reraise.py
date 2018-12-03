def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value... %s" % s)
    #raise用的是默认的错误类型
    return 10/n

def bar():
    try:
        foo("1")
    except ValueError as e: #捕获错误
        print("ValueError!!")
        #ValueError! invalid value 0
        raise #抛出错误

bar()

try:
    10/1
except ZeroDivisionError:
    raise ValueError("input error!")

