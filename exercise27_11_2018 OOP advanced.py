#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" Object Oriented advanced exercise"

__author__ = 'TOA Zhou'



class Student(object):
    pass #类的定义也可以用pass

s = Student()
s.name = "Michael" # 动态给实例绑定一个属性
print(s.name)#Michael

def set_age(self,age):
    self.age =age

from types import MethodType# 定义一个函数作为实例方法
s.set_age=MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25)# 调用实例方法
print(s.age)# 测试结果

s2 =Student()
#s2.set_age(25)
#AttributeError: 'Student' object has no attribute 'set_age'

def set_score(self,score):
    self.score =score

Student.set_score =set_score #把方法赋值给类，而不是执行方法，所以set_score不用括号
#只有在方法或者函数执行的时候，才需要打括号

s.set_score(100)
print(s.score)
s2.set_score(11)
print(s2.score)

class Student(object):
    __slots__ = ("name","age","score")# 用tuple定义允许绑定的属性名称
#slot 空位
s = Student()#创建新的实例
s.name = "ZD"
print(s.name)
s.age = 12
print(s.age)
#s.score =99 #AttributeError: 'Student' object has no attribute 'score'

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score=99
print(g.score)

class GraduateStudent(Student):
    __slots__ = ("sexuality")

g = GraduateStudent()
#g.score=99
#print(g.score) #报错

g.sexuality ="Male"
print(g.sexuality)

s = Student()
s.score = 999999

class Student(object):

    def __init__(self):
        pass

    def set_score(self,value):
        if not isinstance(value,(float,int)):
            raise ValueError("score must be a int or a float")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 and 100")
        self._score = value #虽然可以被访问，但是视为私有变量

    def get_score(self):
        return self._score

s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(10000)#ValueError: score must between 0 and 100

class Student(object):

     @property #加上@property，把一个score.getter方法变成属性
     def score(self):
         return self._score

     @score.setter
     #property同时创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
     def score(self,value):
         if not isinstance(value,(float,int)):
             raise ValueError("score must float or int") #执行中断
         if value < 0 or value >100:
             raise ValueError("score must between 0 and 100")#执行中断
         self._score = value


s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
#函数名为score，所以是写s.score来调用函数
print(s.score) # OK，实际转化为s.get_score()
#函数名为score，所以是写s.score来调用函数
#s.score=111111 #ValueError: score must between 0 and 100



class Student(object):
    @property#加上@property，把一个birth.getter方法变成属性
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value#函数名和变量名重复了,所以加一个下划线

    @property
    def age(self):
        return 2018 - self.birth

s = Student()
s.birth = 1994
print(s.birth,s.age)
#@property广泛应用在类的定义中, 可以让调用者写出简短的代码，同时保证对参数进行必要的检查

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value


    @property
    def resolution(self):
        self._resolution = self._height * self._width
        return self._resolution

s = Screen()
s.width = 1024
s.height = 768

print("resolution = ", s.resolution)
#这么写非常方便
#不用再写s.set_score(60)，print(s.get_score())之类的

class Animal(object):
    pass

#大类

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


class Runnable(Animal):
    def run(self):
        print("Running...")

class Flyable(Animal):
    def fly(self):
        print("Flying...")

class Dog(Mammal,Runnable):
    pass


class Bat(Mammal,Flyable):
    pass

class RunnableMixIn(Animal):
    def run(self):
        print("Running...")

class FlyableMixIn(Animal):
    def fly(self):
        print("Flying...")

class CarnivorousMixIn(Animal):
    def fly(self):
        print("Carnivorous...")

class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass

class Student(object):
    def __init__(self,name):
        self.name =name

print(Student("ZD"))
#<__main__.Student object at 0x000001F3AF75E9E8>
#主函数，的Student 的对象，在xxxx内存


class Student(object):
    def __init__(self,name):
        self.name =name

    def __str__(self):
        return "Student object (name : %s)" % self.name



print(Student("Bob")) #Student object (name : Bob)
print(Student("Bob").name) #Bob

s = Student("Bb")
s

class Fib(object): #一个类可以被用于for...in 循环，类似于list，tuple那样
    def __init__(self):
        self.a,self.b = 0,1# 初始化两个计数器a，b


    def __iter__(self):# 实例self本身就是迭代对象
        #这个类要被循环，就必须实现1个iteration方法
        return self # 返回一个迭代对象。
        # 实例self本身就是迭代对象，因为__next__(self)，故返回自己



    def __next__(self):
        #Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
        self.a,self.b = self.b,self.a +self.b
        if self.a > 1000: #退出循环的条件
            raise StopIteration()
        return self.a# 返回下一个值
        #拿到循环的下一个值。并把它返回,是个int
        #返回的一直都是self.a的值

for n in Fib(): #一个类被用于for...in 循环，类似于list，tuple那样
    print(n) #Fib()循环返回的是个int，根据def __next__(self)的定义

#Fib()[5]
#TypeError: 'Fib' object does not support indexing

class Fib(object):

    def __getitem__(self, n):#循环n次输出
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

f = Fib()
print(f[0],f[3],f[10])#1 3 89

list(range(1,100,10))[2:6]

#list(Fib[2:6]) #TypeError: object() takes no parameters

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int): #n是索引 ,e.g.Fib[3]
            a,b = 1,1
            for x in range(n):
                a,b=b,b+a
            return a
        if isinstance(n,slice): #n是切片,e.g.Fib()[0:5]
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L #返回1个list

print(Fib()[0:5])# [1, 1, 2, 3, 5]
print(Fib()[:6])#[1, 1, 2, 3, 5, 8]
print(Fib()[13])# 377
print(Fib()[0:10:3]) #[1, 2, 3, 5, 8, 13, 21, 34, 55]

class Student(object):

    def __init__(self):
        self.name ="Bob"

s = Student()
print(s.name)
#Bob
#print(s.score)
#AttributeError: 'Student' object has no attribute 'score'

class Student(object):

    def __init__(self):
        self.name = "ZR"

    def __getattr__(self, attr):
        if attr == "score":
            return 99

s = Student()
print(s.name)
#ZR
print(s.score)
#99

class Student(object):
    def __init__(self,birth):
        self.birth =birth
    def __getattr__(self, attr):
        if attr == "age":
            return lambda : 2018 - self.birth
            #不需要传入参数，已经有了

s = Student(1994)
print(s.age()) #24

print(s.abc) #None

class Student(object):

    def __getattr__(self, attr):
        if attr == "age":
            return lambda : 25
        raise AttributeError("\"Student\" object has no attribute \" %s\" " % attr )

s = Student()
print(s.age())
#print(s.abc)
#AttributeError: "Student" object has no attribute " abc"

class Chain(object):

    def __init__(self,path = " "):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" %(self._path,path))
        #链式调用

    def __str__(self):
        return self._path

chain = Chain().status.user.timeline.list
print(chain)
#/status/user/timeline/list

class Student(object):
    def __init__(self,name):
        self.name =name

    def __call__(self, *args, **kwargs):
        print("My name is %s." % self.name)

s = Student("ZZZZ")
print(s(),# self参数不要传入
      s.name) #调用
#对实例进行直接调用


print(callable(s),#对象，可以被调用
      callable(max),#内置函数，可以被调用
      callable([1,2,3]),#list，无法被调用
      callable(None),#空值，无法被调用
      callable("str"))#str，无法被调用
#True True False False False

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(callable(my_abs)) #自定义函数，可以被调用

#Enum的简单写法
from enum import Enum
Month = Enum("Month2",("Jan" ,"Feb",'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month(1))#Month2.Jan
#直接根据value的值获得枚举常量

for name, member in Month.__members__.items(): #key,value,dict
    print(name,"=>",member,",",member.value) #成员名字key，成员，成员的值value

"""
Jan => Month2.Jan , 1
Feb => Month2.Feb , 2
"""


from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon #用成员名称引用枚举常量
print(day1)
#Weekday.Mon
print(day1 == Weekday.Tue) #用成员名称引用枚举常量
#False
print(Weekday.Tue) #用成员名称引用枚举常量
#Weekday.Tue
print(Weekday.Tue.name) #用成员名称引用枚举常量
#Tue
print(Weekday["Tue"]) #用成员名称引用枚举常量
#Weekday.Tue
print(Weekday.Tue.value)#用成员名称引用枚举常量
#2
print(Weekday(3))#直接根据value的值获得枚举常量
#Weekday.Wed
print(Weekday(3)==Weekday.Wed)#直接根据value的值获得枚举常量
#True


#print(Weekday(7))
#ValueError: 7 is not a valid Weekday

for name,member in Weekday.__members__.items():
    print(name, "=>",member,",",member.value)
    #name是成员名称，value是

"""
#项的名字 name => 项.项的名字 member，项.项的值 member.value
Sun => Weekday.Sun , 0 #Weekday.Sum.value == 1
Mon => Weekday.Mon , 1 
Tue => Weekday.Tue , 2
Wed => Weekday.Wed , 3
Thu => Weekday.Thu , 4
Fri => Weekday.Fri , 5
Sat => Weekday.Sat , 6
"""
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

print(Gender.Male)
#Gender.Male

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student("Bart Simpson",Gender.Male)

print(bart.gender)
#Gender.Male



"""
Gender = Enum("_Gender",("_Male","_Female"))

class Student2(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student2("Bart Simpson",Gender._Male)
"""

from hello import Hello #从模块 hello 引入 类 class Hello
h = Hello() #创建类的实例
h.hello("wsss")
#Hello ,wsss
print(type(Hello))
#<class 'type'>
print(type(h))
#<class 'hello.Hello'>


def fn(self,name ="world"):
    print("hhhhhhellooooooo, %s" % name)

Heeeeeeello = type("HHHHHHello",(object,),dict(hellllo=fn)) # 创建Hello class
h = Heeeeeeello()
h.hellllo() # Heeeeeeello 类的方法名称 hellllo
#hhhhhhellooooooo, world



# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name,bases,attrs):
        attrs["add"] = lambda self,value :self.append(value)
        #自己写了个add的方法，加入到类的方法的集合的list里去
        return type.__new__(cls,name,bases,attrs)
        #把add的方法的集合attrs(里面包括自己写的add方法)加入到类的定义里去

class MyList(list,metaclass=ListMetaclass):
    pass

L= MyList()
L.add(1)
print(L)
#[1]
L.append(123)
print(L)
#[1, 123]
L.add(2)
print(L)
#[1, 123, 2]

L2 = list()
#L2.add()
#AttributeError: 'list' object has no attribute 'add'





