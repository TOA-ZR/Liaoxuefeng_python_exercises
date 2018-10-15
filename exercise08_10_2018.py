#!/usr/bin/env python3
c=100+200;
print("hello kit1"); #单引号双引号都可以
print('hello kit2');#Single quotes or double quotes both ok
print("read","the toturial please")#可以接受多个字符串,用逗号“,”隔开
print("100 + 200 =",100+200)
print("please input your name")
variable_name = input();
print(variable_name,"is a genius")
name = input('please enter your name: ')
print('hello,', name)
print("number",0xff00)
print("number1",12e-4)
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
print('I\'m \"ok\" ')
print("I\'m learning what? \nPython")
print("\\\n\\")
print("I\'m learning what? \tPython")
print("\\\t\\")
print(r"\\\t\\")

print('''
    line1
    line2
    line3''')

print(True)
print(False)
print(3>2)
print(1>2)

a=float(input("please input your age")) #input from string to float/int
if a > 18:
    print("adult")
else:
    print("kind")

b = 1
t_2 = "deep learning"
BOOLEAN= True

t_2_copy= t_2
t_2="machine learning"
print(t_2,"t_2")
print(t_2_copy,"t_2_copy")

print('包含中文的str')

ord("A")

birth = float(input("please input the year of your birth"))
if birth >= 2000:
    print("young")
else:
    print("old")

height = 1.91
weight = 83.5
bmi=weight/pow(height,2)
if bmi<18.5:
    print("very thin")
elif 18.5<=bmi<=25:
    print("normal")
elif 25<=bmi<=28:
    print("over weight")
elif 28<=bmi<=32:
    print("fat")
else:
    print("very fat")

sum = 0;
tuplenumer= (1,2,3,4,5,6)
for number in tuplenumer:
    sum=sum + number
print("sum =",sum)

sum2 = 0;
tuplenum=range(5)
for num in list(tuplenum):
    sum2 = sum2 +num
print(sum2)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 101
while n > 0:
    n= n-2
    sum = sum+n
print("while",sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)

n = 1
while n <= 100:
    if n>10:
        break
    print(n)
    n = n + 1
print('END')

n = 1
while n<10:
    n=n+1
    if n%2 ==0 :
        continue
    print(n)
print("end")