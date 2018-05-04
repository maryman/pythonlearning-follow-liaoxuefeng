# -*- coding: utf-8 -*-

# s1=72
# s2=85
# s3=(s2-s1)/s1*100
# print('%.1f%%'%s3)

# print('中文'.encode('gb2312'))

# age=2
# if age>=18:
#     print('your age is %s'%age)
#     print("adult")
# elif age>=6:
#     print('your age is %s' % age)
#     print('teenager')
# else:
#     print('your age is %s'%age)
#     print('kid')

# names=['ma','cao','li']
# for name in names:
#     print(name)

# sum=0
# for x in range(101):
#     sum=sum+x
# print(sum)

# sum=0
# num=100
# while num>0:
#     sum=sum+num
#     num=num-1
# print(sum)

# while 1:
#     print('ma')

# d={'ma':100,'cao':90,'li':80}

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(my_abs('a'))

# import math
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x,y=move(100,100,60,math.pi/6)
# print(x, y)

# import math
# def quadratic(a,b,c):
#     if a==0:
#         x=-c/b
#         return x
#     elif b^2-4*a*c>0:
#         x_1=(-b+math.sqrt(b^2-4*a*c))/(2*a)
#         x_2=(-b-math.sqrt(b^2-4*a*c))/(2*a)
#         return x_1,x_2
#     else:
#         return '无解'
# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))
# print(quadratic(0,1,2))

# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# # person('mali',26,city='beijing',gender='male')
# extra={'city':'beijing','gender':'male'}
# person('mali',26,**extra)

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(998))

# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
# print(fact(999))

