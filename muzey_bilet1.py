# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:28:19 2023

@author: User
"""



print('       Assalomu alaykum,\n      Muzeyga Xush kelibsiz!')
#sa=True
s=''
b="\nSizga bilet narxi "
while s!='exit' and s!='quit':
     print('\n  Dasturni to\'xtatish uchun\n "exit" yoki "quit" so\'zini yozing')
       
     s=input('yoshingizni raqamlar bilan kiriting.>>>')
    
     if s=='exit' or s=='quit':
        print('Dastur tugadi. foydalanganingiz uchun rahmat') 
        
     elif float(s) <= 7: 
        print(b,' 2000 so\'m')
     elif float(s) <= 18:
        print(b,' 3000 so\'m')
     elif float(s) <= 65:
        print(b,' 10000 so\'m')
     else:
        print('Sizga bepul')
       