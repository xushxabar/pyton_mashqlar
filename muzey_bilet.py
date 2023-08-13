# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('       Assalomu alaykum,\n      Muzeyga Xush kelibsiz!')
sa=True
#s=''
b="\nSizga bilet narxi "
while sa:
     print('\n  Dasturni to\'xtatish uchun\n "exit" yoki "quit" so\'zini yozing')
       
     s=input('yoshingizni raqamlar bilan kiriting.>>>')
    
     if s=='exit' or s=='quit':
        print('\n       Dastur tugadi.\n       foydalanganingiz uchun rahmat') 
        sa=False
     elif float(s) <= 7: 
        print(b,' 2000 so\'m')
     elif float(s) <= 18:
        print(b,' 3000 so\'m')
     elif float(s) <= 65:
        print(b,' 10000 so\'m')
     else:
        print('Sizga bepul')
       