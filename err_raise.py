#err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    print("AAA")
    if n == 0:
        raise ValueError("invalid value: %s" % s) #自定义错误类型，用raise抛出
    print("RRR")
    return 10 / n

foo("0")
print("END")


