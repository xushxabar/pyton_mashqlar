# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:57:00 2023

@author: User
"""

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = []
for d in range(3):
    buyurtmalar.append(input(f"{d+1}-buyurtmani bering"))
    
if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")