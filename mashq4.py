# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:55:23 2023

@author: User
"""
#kiritilgan sonni kvadratini va kubini hisoblab chiqarish
son=int(input("Assalomu alaykum, istalgan son kiriting \n>>>>"))
kub=son**3
kvadr=son**2
print(son," ning kvadrati ",str(kvadr)," ga teng.")
print(son," ning kubi ",str(kub)," ga teng.")
#Yoshini so'rab, tug'ilgan yilini hisoblab konsolga cniqaruvchi dastur
yosh=int(input("yoshingiz nechada? \n>>>"))
yil=2023-yosh
print('Demak, siz',yil, 'yilda tug\'ilgansiz')
#foydalanuvchidan ikki son so'rab, sonlarni arifmetik amallarini bajaruvchi dastur
a=float(input('birinchi sonni kiriting\n>>>'.upper()))
b=float(input('ikkinchi sonni kiriting\n>>>'.upper()))
print(f"{a}+{b}=",a+b)
print(f"{a}-{b}=",a-b)
print(f"{a}/{b}=",a/b)
print(f"{a}*{b}=",a*b)