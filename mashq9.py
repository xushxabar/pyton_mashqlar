# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:04:42 2023

@author: User
"""

# juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
s=float(input("Juft son kiriting:\n>>>"))
if s%2==0: print('Rahmat')
else: print('Bu juft son emas')

s=int(input('Yoshingizni kiriting:\n>>>'))
if s<=4 or s>=60:print('Sizga bepul')
elif s<18:print('Sizga 10000 so\'m')
else:print('Sizga 20000 so\'m')

d=float(input('Ikkita son kiriting:\nBirinchi son:'))
s=float(input('Ikkinchi son'))
if d==s: print(d,'=',s)
elif d>s:print(d,'>',s)
else:print(d,'<',s)