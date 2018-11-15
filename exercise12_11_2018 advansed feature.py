
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L3=[L[0],L[1],L[2]]
print(L3)

r = []
n = 3
for i in range(n): #range就是一个整数序列
    r.append(L[i])
print(r)

print(L[0:3])#表示从索引0开始取，直到索引3为止，不包括索引3，即0,1,2 正好3个元素。
print("4",L[:3])#如果第一个索引是0，还可以省略。
print("5",L[1:3])#也可以从索引1开始，取出2个元素
print(L[-2:])# python支持L[-1]取导数第1个元素，那么它同样支持倒数切片
print(L[-2:-1])#从倒数第2个开始到倒数第1个，而不包括倒数第1个

L=list(range(100)) #创建一个0-99的数列
print(L)
print(L[:10])#前10个数。
print(L[-10:])#后10个数。从倒数第十到最后，包括最后-1
print(L[10:20])#前11到20个数。因为第1个数是0，所以第11个数是10
print(L[:10:2])#前10个数，每2个取一个
print(L[::5])#所有数，每5个取1个
print(L[:])#只写[:],原样复制一个list。

print((0,1,2,3,4,5)[:3])#tuple切片

print("ABCDEFG"[:3], #切片字符串string
"ABCDEFG"[::2])



#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
#用的递归方法recursion，碉堡了
def trim(s):
    if (s[:1] == " "):
        s = s[1:]
        s = trim(s)
    elif (s[-1:] == " "):
        s = s[:-1]
        s = trim(s)
    return s


print(trim("                     hello world  "))
print("                     hello world  ")

d={"a":1,"b":2,"c":3}
for key in d:
    print(key)

for value in d:
    print(d[value])

for value in d.values():
    print(value)

for k,v in d.items():
    print(k)
    print(v)

for ch in "ABCDE":
    print(ch)

from collections import Iterable #Python是区分大小写的
print(isinstance([1,2,3],Iterable),
isinstance("string",Iterable),
isinstance((11,12,23),Iterable))

for i,value in enumerate(["T","O","A"]):
    print(i,value)
#T,O,A是变量，下标数字0,1,2索引

#for x,y in [(1,2),(2,3,4),(5,5),("T","O","A")]:
#ValueError: too many values to unpack (expected 2)
#这种错误是指一个tuple值赋给一个tuple变量时，变量个数不够

for x,y in [(1,2),(2,3),(5,5),("T","O")]:
    print(x,y)


#练习
def findMinandMax(L):
    if L == []:
        return (None, None) #返回一个空值
    minv = maxv = L[0]

    for i in L:
      if i>=maxv:
          maxv=i
      if i <= minv:
          minv=i
    return (maxv,minv)

testdata=(1,2,3,4,5,33,1,2)
testdata=[]
print("max = ",findMinandMax(testdata)[0],"min = ",
      findMinandMax(testdata)[1])

#range(1,11)：从1到11但不包括11.
L=list(range(1,11))
print(L)

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

L=[x*x for x in range(1,11)]
print("repeat",L)

L=[]
for m in "ABC":
    for n in "DEF":
        L.append(m+n)
print(L)

L=[m + n for m in "ACB" for n in "TOA"]
print(L)

import os #导入os模块，模块的概念后面讲到
L=[d for d in os.listdir(".")]#os.listdir可以列出文件和目录
print(L)

d={"x": "T", "y": "O", "z": "A"}
for key,value in d.items():
    print(key,"=", value)

L=[key + "=>" + value for key, value in d.items()]
print(L)

L = [s.lower() for s in L]
print(L)

x = "abc"
y = 123
print(isinstance(x, str),
isinstance(y, str))

L = ['Hello', 'World', 18, 'Apple', None]
M=[]
for item in L:
    if isinstance(item,str) is True:
        item = item.lower()
        M.append(item)
    else:
        M.append(item) #加上这个就保留数字，不加就只有小写字母。
L=M
print(L)

L2 = [s.lower() for s in L if isinstance(s, str)]
#推荐写法，list comprehension

L1 = [x*x for x in range(10)]
g1 =(x*x for x in range(10))
print(g1) #因为保存的是算法，所以打印出来的不识数，而是这个：<generator object <genexpr> at 0x000001E6759BEA98>
print(next(g1),next(g1),next(g1))
print(next(g1),next(g1),next(g1))

g1=(x*x for x in range(10))
for x in g1:
    print(x)


def fib(max):
    n,a,b=0,0,1
    while n< max:
        print(b)
        a, b= b, a+b #赋值语句
        n+=1
    return "done"

fib(10)

def fib(max):
    n, a, b = 0, 0, 1
    while n< max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6)) #只会显示generator object
for i in fib(6):#正确print generator内容的写法
    print(i)


def odd(): #没有input ，调用next的时候执行函数
    print("step 1")
    yield 1#遇到yield语句就返回。等到下次调用的时候从上次返回的yield语句处执行
    print("step 2")#再次遇到next语句。执行函数，从这里开始。
    yield 3 #遇到yield语句就返回。
    print("step 3")#再次遇到next语句。执行函数，从这里开始。
    yield 5 #遇到yield语句就返回。

o=odd()#调用该generator时，首先要生成一个generator对象，

#next(o)
print(next(o))#然后用next不断获得下一个返回值。
#next(o)
print(next(o))
#next(o)
print(next(o))
#print(next(o))#没有yield可以执行了，开始报错。

for i in odd(): #用for loop也可以实现对这个generator的调用
    print(i)


g = fib(7)
while True:
    try:
        x = next(g)
        print("g: ",x)
    except StopIteration as e:
        print("Generator return value:" ,e.value)
        break #直接退出循环


w= fib(8)
for i in w:
    try:
        print("w:" ,i)
    except StopIteration as e:
        print("Return Value is:", e.value)
        break
'''
'''#杨辉三角
def triangle(max):
    a=[1]
    n=0
    while n<max:
        yield a
        a = [x+y for x,y in zip(a+[0],[0]+a)]
        #变成tuple
        #列表生成式，功用和a.append相同。
        n+=1

for i in triangle(10):
    print(i)




def triangles():
    #利用生成器(yield)使得每次调用的时候分配内存避免开辟过大内存
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i] + N[i - 1] for i in range(len(N))]
        #list(range(1))=[0] 到1但是不包括1
        #list(range(2))=[0, 1] 到2但是不包括2


if __name__ == "__main__":
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break

def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
        #[1]+[1]=[1, 1] tuple合并
        #[1, 1][0]+[1, 1][1]=1+1=2 数值相加
        # list(range(1))=[0] 到1但是不包括1
        # list(range(2))=[0, 1] 到2但是不包括2



n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


from collections import Iterator

print(isinstance([], Iterable),#list, Iterable
      isinstance({}, Iterable),#tuple
      isinstance('abc', Iterable),#string
      isinstance((x for x in range(10)), Iterable),#generator
      isinstance(100, Iterable))#int

#Function iter()
print(isinstance([],Iterator), #not Iterator
      isinstance(iter([]),Iterator),#Iterator
      isinstance("abc",Iterator),#not Iterator
      isinstance(iter("abc"),Iterator),#Iterator
      isinstance((x for x in range(10)), Iterator))#Iterator

for x in list(range(5)):
    pass

# 首先获得Iterator对象:
it = iter(list(range(5)))
# 循环:
while True:
    try:
        x =next(it)
        #print(x)
    except StopIteration:
        break


