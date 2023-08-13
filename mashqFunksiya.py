# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:43:54 2023

@author: User
"""
print('assalomu alaykum')
def sof():
    """Foydalanuvchi ismi va yoshini so'rab,
    uning tug'ilgan yilini hisoblaydigan funksiya """
    ism=input('ismingizni yozing.>>>')
    yos=input(f'Assalomu alaykum {ism.title()}, yoshingiz nechada?>>>')
    print(f'{ism.title()}, siz {2023-int(yos)} yili tug\'ilgansiz')
    
#sof() 
def son(x,y=2):
    """ son olib, uning kvadrati va,
    kubini, istalgan darajasini konsolga,
    chiqaruvchi funksiya"""
    print(f'{x} ning {y}-darajasi {x**y} ga teng')
while True:
    x=int(input('son kiriting >>'))
    if x==0:
          break
    y=int(input(f'{x} ning darajasini kiriting >>'))
    if y==0:
          break  
    son(x,y)
sof()
   