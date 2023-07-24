# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:42:26 2023

@author: User
"""


mahsulotlar=['banan','olma','uzum','non','sut','shakar','choy','tarvuz','qovun','limon']
savat=[]
do=[]
for n in range(5):
      savat.append(input(f"{n+1} - mahsulot kiriting ")) 
      d=savat.pop()
      if d in mahsulotlar:
         savat.append(d)     
         print(f'{d} do\'konda bor')
        
      else:
          do.append(d)
          print(f' {d} yoq')
if len(do)==5:
    print('Siz soragan mahsulotlar dokonda yoq')
elif len(do)==0:print('Siz soragan barcha mahsulotlar bor')
else:
         print(f'{[do]}  yoq')  
         print(f'{[savat]}  bor')      