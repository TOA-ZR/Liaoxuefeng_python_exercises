abs(-12)
max(1,2,3,4,777,884,4,2,77,45,)
int(123.3444)
int("1112")
#int("1112.3") 这么写不行，会报错。
float("233.1")
str(1000)
bool(1123)
bool("")
bool("0")#True

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-99))#调用函数

def nop():
    pass

age=19
if age>= 18:
    pass

#plus isinstance
def my_abs1(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x
print(my_abs1(-222))

import math

def move(x,y,step,angle=0):#弧度制
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

x, y = move(100, 100, 60, math.pi / 6) #输入的是一个弧度，而不是角度
print(x,y)

r = move(100, 100, 60, math.pi / 6)
print("r =",r)

#practise
import numpy as np
def quadratic(a,b,c):
    print("%dx^2+%dx+%d"%(a,b,c))
    s = b*b-4*a*c
    if s >= 0 and a != 0:
        x1 = np.float((-b+math.sqrt(b*b-4*a*c)))/np.float((2*a))
        x2 = np.float((-b-math.sqrt(b*b-4*a*c)))/np.float((2*a))
    else:
        print("no result")
    return x1,x2
x1,x2=quadratic(2,55,3)
print(x1,x2)

def power(x):
    return x*x
print(power(5))

def power1(x,n):
    s = 1
    while(n):
        n=n-1
        s=s*x
    return s
print(power1(5,3))

def power2(x,n=2):
    s = 1
    while(n):
        n=n-1
        s=s*x
    return s
print(power2(6))

def enroll(name,gender):
    if not (isinstance(name,str) and isinstance(gender,str)) :
        raise TypeError("bad operand type")
    print("name :",name)
    print("gender:",gender)

enroll("aaa","F")

def enroll(name,gender,age=19,city= "Dalian"):
    if not (isinstance(name,str) and isinstance(gender,str)and isinstance(age,int)and isinstance(city,str)):
        raise TypeError("bad operand type")
    print("name :",name)
    print("gender :",gender)
    print("age :",age)
    print("city :",city)

enroll("aaa","F")

def add_end(L=[]):
    L.append("END")
    return L
print(add_end([1,2,3]),
add_end(["x","y","z"]),
add_end(),
add_end(),
add_end(),
add_end(["x","y","z"]))


def add_end(L=None):
    if L is None:
        L = []
    L.append("END")
    return L
print(add_end([1,2,3]),
add_end(["x","y","z"]),
add_end(),
add_end(),
add_end(),
add_end(["x","y","z"]))

def calc(number):
    sum = 0
    for n in number:
        sum = sum +n * n
    return sum

print(calc([1,2,3]),
calc((1,2,3)))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3))

num = [1,3,5]
print(calc(num[0],num[1],num[2])
,calc(*num))

#关键字参数
def person(name,age,**kw):
    print("name :",name,"age :",age,"other :",kw)

person("Zhou",17,city="Peking",job="Engineer")
person("Zhou",17)

extra = {"city":"Shanghai","job":"Programmer"}
person("Zhou",17,city=extra["city"],job=extra["job"])

person("Zhou",17,**extra)

def person(name,age,**kw):
    if "city" in kw:
        print("city input")
    if "job" in kw:
        print("job input")
    print("name :",name,"age :",age,"other :",kw)

person("Zhou",17,**extra)

def person(name,age,*,city,job):
    print(name,age,city,job)
person("Zhou", 17, **extra)
person("Xu",14,city="Karlsruhe",job="Engineer")

def person(name,age,*,city="Karlsruhe",job):
    print(name,age,city,job)

person("Zhou", 17, **extra)
person("Xu",14,job="Engineer")

# 5 kinds of parameter mix use
def f1(a,b,c=0,*arg,**kw):
    print("a =",a,"b =",b,"c=",c,"arg =",arg, "kw=" ,kw)

f1(1,2,3,4,5)

def f2(a,b,*,d,**kw):
    print("a=",a,"b=",b,"d=",d,"kw=",kw)
f2(1,2,d=3,ext=[4,5])

arg=(1,5)
kw={"d":4,"kwk": 444}
f1(*arg,**kw)
f2(*arg,**kw)

def product(*x):
    sum = 1
    for i in x:
        sum =sum*i
    return sum

print(product(1,2,3,4,5))

def test(a,b,*c,e,d):
    print("a=",a,"b=",b,"c=",c,"e=",e,"d=",d)

test(1,2,3,45,4,3,21,1,5,23,e=1,d=2)

#recursion
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(10))
#fact(1000)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

#汉诺塔的移动
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')


