# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 18:19:29 2023

@author: User
"""

cars=[]
cars.append('bmw')
cars.append('malibu')
cars.append('volvo')
print(cars)
print(cars[0].upper())
cars.append('mers')
cars.insert(3,'mersedes')
print(cars)
d=cars.pop(2)
print(cars)
cars.insert(0,d)
print(cars)
q=input('biror mashina markasini kirit\n>>>')
cars.append(q)
print(cars)
#ro'yhat tuzib konsolga chiqarish
ismlar=[]
ismlar.append('ozod')
ismlar.append('nodir')
ismlar.append('komol')
ismlar.append('said')
print('asssalomu alaykum, ',ismlar[0],'yahshimisan? Bugun coyxona bormi?')
print('asssalomu alaykum, ',ismlar[1],'yahshimisan? Bugun coyxonaga borasanmi?')
print('asssalomu alaykum, ',ismlar[3],'yahshimisan, bugun coyxonaga bordingmi?')
#sonlar r'yhati
sonlar=[]
sonlar.append(23)
sonlar.append(567)
sonlar.append(-35)
sonlar.append(5.76)
t=sonlar[0]*sonlar[3]*3
f=sonlar[1]+t/sonlar[3]
print('t=',t)
print('f=',f)
sonlar[0]=sonlar[3]+2.24
sonlar[1]=sonlar[1]-500
print(sonlar)
s=sonlar.pop(2)
print(s)
print('men ',sonlar.pop(1)+2,'ta mashinam bo\'lishini orzu qilaman')
ismlar.append(cars.pop(0))
print(ismlar)
