# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main() #这个程序里没有try，所以不会捕获错误，而是让python解释器直接打印出错误堆栈
print("END")