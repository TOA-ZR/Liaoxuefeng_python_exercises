#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" Object Oriented Programming for short OOP"

__author__ = 'TOA Zhou'

std1 = {"name": "Zhou","score": 100} #dict
std2 = {"name": "Liu","score": 90}

def print_score(std):
    print("%s: %s" % (std["name"],std["score"]))

print_score(std1)

class Student(object):

    def __init__(self,name,score):#初始化类
        self.name = name
        self.score = score

    def print_score(self):
        print("%s: %s" % (self.name, self.score))


bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 91)
bart.print_score()
lisa.print_score()

class Student(object):#类名都用大写字母开头
    #括号里是继承的类，没有就用object
    pass

lei  = Student
print(lei)#<class '__main__.Student'> 变量指向类
print(Student)#<class '__main__.Student'> 是一个类
bart = Student()#创建Student的实例
print(bart)#<__main__.Student object at 0x0000024CA0F85860>  变量指向对象

bart.name = "Bart Simpsomn"
print(bart.name)

class Student(object):

    def __init__(self, name, score):
        #特殊的__init__方法, 建实例的时候，就把name，score等属性绑上去
        self.name = name
        self.score = score

    def print_score(self):
        print("%s: %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >=60:
            return "B"
        else:
            return "C"


bart = Student("Bart Simpsonn",66)#不写全了会报错
print(bart.score)

def print_score(std):
    print("%s: %s" % (std.name, std.score))

print_score(bart) #Bart Simpsonn: 66

bart.print_score()#Bart Simpsonn: 66

lisa = Student("Lisa Simpson",100)
bart = Student("Bart Simpson",50)

lisa.print_score()#Lisa Simpson: 100
print(lisa.get_grade())#A

bart.age = 8
print(bart.age) #8
#print(lisa.age) #AttributeError: 'Student' object has no attribute 'age'

zhou = Student("TOA Zhou",1.0)
print(zhou.score) #1.0
zhou.score = 1.7
print(zhou.score) #1.7

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %s" % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score): #self这个变量就是实例本身，不用输入
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")
            #raise是什么？ 感觉是个报错的东西，之后报错那张应该会讲。





Liu = Student("Liu Ning",100)
#print(Liu.__name) #AttributeError: 'Student' object has no attribute '__name'

#Liu.set_score(333) ValueError: bad score

print(Liu._Student__name)
print(Liu.get_name())

Gong = Student("Gong Zijie",34)
print(Gong.get_name())# Gong Zijie
Gong.__name = "New Name"
print(Gong.__name)# New Name

# get_name()内部返回self.__name
print(Gong.get_name())# Gong Zijie

class Student(object):

    def __init__(self,name,gender):#初始化类
        self.__name = name
        self.__gender = gender

    def set_gender(self,gender):
        self.__gender= gender

    def get_gender(self):
        return self.__gender


Xu = Student("Xu Kailing","Female")
print(Xu.get_gender())
Xu.set_gender("male")
print(Xu.get_gender())


class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()#创建一个实例要打括号
dog.run() #Animal is running...


cat=Cat()
cat.run()#Animal is running...

class Dog(Animal):

    def run(self):
        print("Dog is running")

    def eat(self):
        print("Eating meat...")

class Cat(Animal):

    def run(self):
        print("Cat is running")

dog = Dog()#创建一个实例要打括号
dog.run() #Animal is running...


cat=Cat()
cat.run()#Animal is running...

class Dog(Animal):

    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

dog = Dog()#创建一个实例要打括号
dog.run() #Animal is running... 调用类中的方法


cat=Cat()#创建一个实例要打括号
cat.run()#Animal is running...调用类中的方法


a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型


print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))

b = Animal()
print(isinstance(b, Dog))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())#Animal()相当于创建了一个Animal类，只是没有赋值给变量。
run_twice(Dog())#Dog()相当于创建了一个Dog类，只是没有赋值给变量。
run_twice(Cat())#Cat()相当于创建了一个Cat类，只是没有赋值给变量。
"""
Dog is running
Dog is running
Cat is running
Cat is running
Tortoise is running slowly...
Tortoise is running slowly...
"""
class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly...")

run_twice(Tortoise())

class TOA(object):

    def run(self):
        print("Timer is running...")

run_twice(TOA())

#基本类型都可以用type()判断：
print(type(123),#<class 'int'>
      type("string"),#<class 'str'>
      type(None),#<type(None) 'NoneType'>
      type(abs),#<class 'builtin_function_or_method'>
      )

c= Dog()
print("c= Dog()",type(abs),#<class 'builtin_function_or_method'>
      type(c),#<class '__main__.Animal'>
      type(c)==Animal)#False

print(type(123)==type(234),#True
      type(123) == int,#True
      type("123") == str,#True
      type("str")==type(123))#False
print()
print()

import types
def fn():
    pass

#Function; BuiltinFuntion;Lambda;Generator
print(type(fn) == types.FunctionType,
      type(abs) == types.BuiltinFunctionType,
      type(lambda x: x) == types.LambdaType,
      type(x for x in range(0)) == types.GeneratorType)#生成器
#True True True True


class Husky(Dog):

    def run(self):
        print("Husky is running...")


a = Animal()
b = Dog()
c = Husky()

print(isinstance(c,Husky), #True
      isinstance(c,Dog),#True
      isinstance(c,Animal))#True

print(isinstance(b,Animal) and isinstance(b,Dog),#True
      isinstance(b,Husky))#False

print(isinstance("a",str),
      isinstance(123,int),
      isinstance(b"a",bytes))

print(isinstance([1,2,3],(list,tuple)),#True
      isinstance((1,2,3),(list,tuple)))#True

print(type(c)==Husky,#True
      type(c) == Dog)#False

print(dir("ABC")) #"ABC"是一个对象
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print(len("ABC"))
print("ABC".__len__())

class myDog(object):
    def __len__(self):
        return 10

dog = myDog()
print(len(dog)) #10


print("ABC".lower())#abc


class MyObject():
    def __init__(self): #属性的初始化
        self.x = 9

    def power(self):
        return self.x *self.x

obj = MyObject()

print(hasattr(obj,"x"),#True # 有属性'x'吗？
      obj.x,#9
      hasattr(obj,"y"),#False # 有属性'y'吗？
      setattr(obj,"y",16),#None # 设置一个属性'y'
      hasattr(obj,"y"),#True # 有属性'y'吗？
      getattr(obj,"y"),#16 # 获取属性'y'
      obj.y,
      getattr(obj,"y",22)) #16 # 获取属性'y'
        #如果属性不存在，就返回默认值22, 如果属性存在，返回属性值16

print(getattr(obj,"z",33)) #33
#AttributeError: 'MyObject' object has no attribute 'z'


obj2=MyObject()
#print(getattr(obj2,"y"))#报错
#这个只是给控制一个对象的变量，而不能改变类本身

print(hasattr(obj,"power"), #True # 有属性'power'吗？
      getattr(obj,"power"),) # 获取属性'power'
#<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>

fn =getattr(obj,"power")# 获取属性'power'并赋值到变量fn
print(fn)# fn指向obj.power这个方法
#<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
print(fn(),# 调用fn()与调用obj.power()是一样的
      obj.power())# 调用fn()与调用obj.power()是一样的

sum = obj.x +obj.y
print(sum)
sum = getattr(obj,"x")+getattr(obj,"y")
print(sum)


class Student(object):
    def __init__(self,name):
        self.name =name #通过self变量，給实例绑定属性


s = Student("Bob")
s.score = 90 #通过实例变量，給实例绑定属性
print(s.score) #90

class Student(object):
    name = "Student" #給Student类本身绑定一个属性

s = Student() #创建一个实例s
print(s.name)
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)# 打印类的name属性
#Student
s.name = "Michael"  # 给实例绑定name属性
print(s.name) #Michael
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)#Student
# 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name)#Student
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

class Student(object):

    count = 0 #Student.count 定义了一个类属性

    def __init__(self,name):
        self.name = name
        Student.count+=1


print(Student.count)
bart = Student("Bart")
print(Student.count)
lisa = Student("Lisa")
print(Student.count)