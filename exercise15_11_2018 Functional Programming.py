print(abs(-10),#调用该函数
      abs)#函数本身 build in function
a=abs #可以把把函数本身赋值给变量
x=abs(-10)#要获得函数调用结果，我们可以把结果赋值给变量
print(a,x,
      a(-2))#如果一个变量指向了一个函数，那么，可以通过该变量来调用这个函数的
#成功，说明a现在已经指向了abs函数本身。直接调用abs()函数和调用变量a()完全相同

#abs=10
#abs(-10)
#import builtins
#builtins.abs=10

def add(x,y,f):
    return f(x)+f(y)

print(add(-4,-5,abs))#9

'''
x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
'''

c=[]
for i in (x*x for x in range(9)):
    c.append(i)
print(c)

from collections import Iterator
def f(x):
    return  x*x
r = map(f,list(range(10)))
print(r) #map object
print(isinstance(r,Iterator))# map object is Iterator
print(list(r))#用list，让Iterator把整个序列都计算出来。贼方便。
#Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

print(list(map(str,range(1,10))))
print(list(map(str,list(range(1,10)))))
#因为range和list都是Iterable,所以map结果是一样的

from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,range(1,10)))
print(reduce(add,list(range(1,10))))

def fn(x,y):
    return x*10+y
re=reduce(fn,range(1,10,2))
print(re)

def char2num(s):
    digits={"0":0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(list(map(char2num,"2333333")))#map出来的是个Iterator，通过list，转化成了个list

test="12345"
print(reduce(fn,map(char2num,test)))

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))

def normalize(name):

        if isinstance(name, str) is True:
            item = name.lower()
        return item

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def multi(x,y):
        return x*y
    return reduce(multi,L)
print('3 * 5 * 7 * 9 =', prod([3, 1, 7, 10]))

'''
def str2float(L):
    from functools import reduce
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,".":-1}
    def str2num(L):
        return DIGITS[L]
    def num2float(x,y):
            return 10*x+y
    return reduce(num2float,map(str2num,L))#reduce对于map的作用和list有点像，也是让map迭代到最后。

print("123.234","=",str2float("123.234"))
'''

def str2float(s):
    def left(x,y):
        return x*10+y
    def right(x,y):
        return 0.1*x+y
    def str2int(s):
        digits={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'.':'.'}
        return digits[s]
    p=s.find('.')
    ql=s[:p]
    qr=s[:-p-1:-1]#-1到-p-1,不包括-p-1,倒着输出的。
    return reduce(left,map(str2int,ql))+0.1*reduce(right,map(str2int,qr))
print("123.234","=",str2float("123.234"))


def is_odd(n):
    return n % 2 == 1 #只有True的时候才返回 n
    pass
print("odd number ：",list(filter(is_odd,list(range(1,15)))))

def not_empty(s):
    return s and s.strip() #s 和 去除空格的s的交集，有交集就返回s
#应该是只能返回输入的
print(list(filter(not_empty,["    a","    ",None,"o"])))


def odd_iter():
    n=1
    while True:
        n+=2
        yield n #3,5,7,9...

print("odd:",next(odd_iter()))

def _not_divisible(n):
    return lambda x: x % n > 0
    #lambda，匿名函数，只使用一次的函数
    #return True or False，跟上面那个一样，用在Filter里,True return x int,False dont return



def primes():
    yield 2
    it = odd_iter() # 初始序列，变量指向这个generator
    while True:
        n = next(it) #执行generator，返回序列的第一个数:3
        yield n #return 3
        it = filter(_not_divisible(n), it) # 构造新序列
        # it is a odd list
        # it = filter((x: x%3>0,[3]), odd_iter()) 只保留无法整除的数
        # it = filter(filter((x: x%5>0,[5]),filter((x: x%3>0,[3]), odd_iter()))
        #不断地加filter的筛选条件，generator也因为循环不断地扩大。感觉是每次it根据generator变大，都要把所有条件轮一遍
# 打印1000以内的素数:
for i in primes():
    if i < 1000:#循环次数
         print(i)
    else:
        break


def is_palindrome(n):
    return str(n)[::]==str(n)[::-1]

print(list(filter(is_palindrome,range(1,200))))

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21],key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#['Credit', 'Zoo', 'about', 'bob']

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#['about', 'bob', 'Credit', 'Zoo']


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
#['Zoo', 'Credit', 'bob', 'about']

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#这个不是一个dict，是一个tuple，不能用.value, .key. .item。而是用[0].[1]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
#[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]



def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
#[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]



def calc_sum(*args): #可变参数(不限制个数，组成一个tuple)的求和
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3,4,5))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,2223,4,6)
print(f)#<function lazy_sum.<locals>.sum at 0x000001E3BAA95AE8>
print(f())#2236
print("f()= ",lazy_sum(1,2,2223,4,6)())#f()=2236



f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i #每次循环，都创建都创建一个新函数，
        #一共循环3次，创建3个函数
        fs.append(f)
    return fs #返回的是三个函数f()组成的list
    #最后执行的时候代入的i是3

f1,f2,f3=count()#把创建的3个函数都返回了
print("f1,f2,f3 =",f1(),f2(),f3())

F = count() #函数也可以作为一个对象，放在一个list里面。
print("F=",F[0](),F[1](),F[2]())


def count():

    def f(j): #再创建一个函数
        #用该函数的参数(j)绑定循环变量的当前的值
        #无论该循环变量(j)后续如何更改，已绑定到函数f(j)参数的值不变。

        def g():
            return j*j
        return g

    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i)立刻被执行，因为带括号()。因此i的当前值被传入f()，然后出结果，加到fs里面

    return fs #返回的是三个执行f(1),f(2),f(3)之后组成的数值的list
    #最后执行的时候是输出的是一个有了绑定的输入值的函数的list
    #虽然返回的还是函数，但是函数的输入值已经由j确定了。

f1,f2,f3=count()#把创建的3个函数都返回了,每个函数的输入值已经确定，并且不同
print("f1,f2,f3 =",f1(),f2(),f3())

def createCounter():
    ans = [0]
    print(ans)
    def counter():
        ans[0] += 1 #引用局部变量ans[0]
        print(ans)
        return ans[0]
    return counter #返回一个函数，不立即执行。
#这个函数返回的是counter，所以执行它的时候实际上是在执行counter()。
# counter只是一开始调用了ans = [0]的局部变量，之后在它的内部就不断地在给ans更新
#counter 内部自己的ans在不断地变化。返回的是counter内部的ans值，而不是createCounter内部ans = [0]的值

counterA = createCounter() #把函数createCounter()赋给了变量counterA
print("counter =", counterA(), counterA(), counterA(), counterA())
print("counter =", counterA(), counterA(), counterA(), counterA())
#要执行这个createCounter(),要给counterA后面加括号()。

print(list(map(lambda x:x*x,range(1,10))))

def f(x):
    return x*x
print(list(map(f,range(1,10))))

square= lambda x: x*x #匿名函数赋值给一个变量
print(f)#<function f at 0x000001DE4E1C4D08>
print(f(5))#25 #利用变量来调用该函数

def build(x, y):
    return lambda: x * x + y * y

f=build(2,3) #赋值的是一个函数，相当于一个返回函数。
#返回函数一定要在函数里赋值才能正确使用。参数就固定下来了
print(f) #<function build.<locals>.<lambda> at 0x0000029A48BD81E0>
print(f())#13

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

#写成匿名函数
L = list(filter(lambda n:n%2==1, range(1, 20)))
#冒号前面的 n 表示函数参数
#只有一个表达式n%2==1，返回值就是该表达式子的结果
#用了filter，根据返回值是True还是False决定保留还是丢弃该元素 n
print(L)

def now():
    print('2018-11-20')
f=now
f() #2018-11-20
print(f) #<function now at 0x0000028A79E756A8>

print(now.__name__)#name of the function now
print(f.__name__)#name of the function now

def log(func):
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)#首先打印日志
        return func(*args,**kw)#再紧接着调用原始函数
    return wrapper #log返回一个函数 所以log是一个高阶函数

@log
def now():
    print('2018-11-19')

now()#执行
#call now():
# 2018-11-19
print("1",now.__name__)
#1 wrapper

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute")
def now():
    print('2018-11-18')

now()#执行
#execute now():
#2015-3-25

print(now.__name__)
#wrapper
#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'


import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s();" % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-11-17')

now()
print(now.__name__)


import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():" %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log("functool")
def now():
    print('2018-11-18')

now()
print(now.__name__)

import time, functools

#Decorator
def metric(fn):
    print("%s executed in %s ms" % (fn.__name__,10.24))
    return fn

@metric
def fast(x,y):
    time.sleep(0.012)
    return x+y

f=fast(11,22)
print(f==33)



def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.clock() #time.perf_counter()
        c=fn(*args, **kw)
        end = time.clock() #time.perf_counter()
        print('%s executed in %s ms' % (fn.__name__, (end-start)*1000))
        return  c #带参数返回的是一个值，不带参数返回去是一个函数变量
    return wrapper

@metric #额外附加的，返回执行时间的功能。不改变原有函数。
def fast(x,y):
    time.sleep(0.012)
    print("111111")
    return x+y #返回的是一个值，不是一个函数。
# fast(x+y)=metric(fast(x+y))

f=fast(11,22)
print(f)

print(int("12345"),#int()函数默认按十进制转换
      int("12345",base=8),#int()函数还提供额外的base参数
      int("12345",16))

def int2(x, base=2):
    return int(x,base=base) # int(x,base)也可以

print(int2("1000000"))#64
print(int2("1010101"))#85

import functools
int2 = functools.partial(int,base=2)
print(int2("1000000"))#64
print(int2("1010101"))#85

print(int2('1000000', base=10))#1000000

print(int2('10010'))
kw = { 'base': 2 }
int('10010', **kw)
#int2 = functools.partial(int,base=2) 一个意思，dict
print(int('10010', **kw))#kw = { 'base': 2 }相当于base=2


max2 = functools.partial(max, 10)
#10是个*args，*args是可变参数，args接收的是一个tuple
max2(5, 6, 7)
#上下一个意思
args=(10,5,6,7)
print(max(*args))

