#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" Object Oriented advanced exercise"

__author__ = 'TOA Zhou'

f=open("./test.txt","r")

#f=open("./test1.txt","r")

f.read()#返回一个str对象
print(f.read())#打印一个str对象,
f.close()

try:
    f = open("./test.txt", "r")
    print(f.read())#打印一个str对象
finally:
    if f:
        f.close()

with open("./test.txt", "r") as f:
    print(f.read())



f = open("./test.txt", "r")
for line in f.readlines(): #f.readlines()是一个list，每一行是一项
    print(line.strip())  # 把末尾的'\n'删掉

print(f.read(1))

print(f.readline())

f = open("./test.jpg","rb")
#print(f.read())# 十六进制表示的字节

f = open("./testchi.txt",'r',encoding="gbk")

f=open("./test.txt","w")
f.write("Hello,IPR") #直接把test文档里的内容都去掉，然后写入。
f.close()
f=open("./test.txt","r")
for line in f.readlines():
    print(line)
f.close()

with open("./test.txt","w")as f:
#with open("./test.txt","w",encoding="gbk")as f:
    f.write("Hello,World")


fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open(fpath,"r") as f:
    for line in f.readlines():
        print(line)
#观察结果


from io import StringIO
f = StringIO() #创建一个StringIO
f.write("hello")#像文件一样写入
f.write(" ")
f.write("world!!")
f.write("\n你好世界")
print(f.getvalue())#getvalue()方法用于获得写入后的str。
#hello world!!



from io import StringIO
f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f.readline()#每次读一行。不断循环
    if s == "":
        break #程序中断
    print(s.strip())# 把末尾的'\n'删掉，不会再多跳一行
"""
Hello!
Hi!
Goodbye!
"""

from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87'

import os
os.name #操作系统的类型
print(os.name)
#nt
#os.uname()
os.environ
print(os.environ)

os.environ.get("PATH")
print(os.environ.get("PATH"))
#'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
os.environ.get("x","default")
print(os.environ.get("x","default"))
#default

# 查看当前目录的绝对路径:
os.path.abspath(".")
#C:\Users\jo\PycharmProjects\liaoxuefeng_exercises
print(os.path.abspath("."))
'''
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
'''
os.path.split('/Users/michael/testdir/file.txt')
print(os.path.split('/Users/michael/testdir/file.txt'))
#('/Users/michael/testdir', 'file.txt')

os.path.splitext('/path/to/file.txt')
print(os.path.splitext('/path/to/file.txt'))
#('/path/to/file', '.txt')

# 对文件重命名:
#os.rename("test.txt","test2.py")
# 删掉文件:
#os.remove("test2.py")

ditlis=[x for x in os.listdir(".")if os.path.isdir(x)]
print(ditlis)
#['.git', '.idea', 'venv', '__pycache__']

pyfile=[x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[-1]==".py"]
print(pyfile)
#['err.py', 'err_logging.py', 'err_pdbtest.py', 'err_raise.py', 'exercise08_10_2018.py', 'exercise12_11_2018 advansed feature.py', 'exercise15_11_2018 Functional Programming.py', 'exercise21_11_2018 Module.py', 'exercise21_11_2018 OOP.py', 'exercise24_10_2018.py', 'exercise27_11_2018 OOP advanced.py', 'exercise28_11_2018 error adjust test.py', 'exercise5_12_2018 IO Programming.py', 'fact.py', 'hello.py', 'mydict.py', 'mydict2.py', 'mydict_test.py', 'newhello.py', 'reraise.py', 'student.py', 'student_test.py', 'test.py', 'test2.py', '__init__.py']

import os
def find(path,str):
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path,x)):
            find(os.path.join(path,x),str)

        if os.path.isfile(os.path.join(path,x)):
            if str in os.path.splitext(os.path.join(path,x))[0]: #如果str在这个路径中
                print(os.path.join(path, x))

#单元测试
def test():
    find(".", "test")

if __name__ == '__main__':
    pass
    #test()



d = dict(name="Bob",age=20,score=88)

import pickle
d = dict(name="Bob",age=20,score=88)
pickle.dumps(d)
print(pickle.dumps(d))
#b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x05\x00\x00\x00scoreq\x03KXX\x03\x00\x00\x00ageq\x04K\x14u.'

f = open("dump.txt","wb")
pickle.dump(d,f)

f.close()




f=open("dump.txt","rb")
d = pickle.load(f)
print(d)
#{'age': 20, 'score': 88, 'name': 'Bob'}

import json
d = dict(name="Bob",age=20,score=88)
print(d)
#{'score': 88, 'age': 20, 'name': 'Bob'}
json.dumps(d)
print(json.dumps(d))
#{"score": 88, "age": 20, "name": "Bob"}

json_str=json.dumps(d)
json.loads(json_str)
print(json.loads(json_str))#把JSON的字符串反序列化
#{'score': 88, 'age': 20, 'name': 'Bob'}

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student("Bob",2,88)
#print(json.dumps(s))#定义Student类，然后序列化


def student2dict(std):
    return{"name" : std.name,
           "age" : std.age,
           "score": std.score
           }
json.dumps(s,default=student2dict)
print(json.dumps(s,default=student2dict))
#{"name": "Bob", "age": 2, "score": 88}

print(json.dumps(s,default = lambda obj:obj.__dict__))#把s.__dict__赋值给s
#{"score": 88, "name": "Bob", "age": 2}

print("liangliang",s.__dict__)
#liangliang {'age': 2, 'score': 88, 'name': 'Bob'}

def dict2student(d):
    return Student(d["name"],d["age"],d["score"])

json_str = json.dumps(s,default = lambda obj:obj.__dict__)
print(json.loads(json_str,object_hook=dict2student))
#<__main__.Student object at 0x00000283792BB048>
#打印出来的是反序列画的Student实例对象

import json
obj = dict(name = "小明",age=20)
s = json.dumps(obj,ensure_ascii=False)
print(s)