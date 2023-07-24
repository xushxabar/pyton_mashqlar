# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:20:08 2023

@author: User
"""

mahsulotlar = ['un', 'yog\'', 'sovun', 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat=[]

for n in range(3):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
if savat==True:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            