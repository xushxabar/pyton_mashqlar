<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:39:52 2023

@author: User
"""

taom={'ali':'osh',
      'karim':'makaron',
      'salim':'shokolad',
      'qobil':'lapsha'}
print(taom.keys())
#print('Bizda Ali,Karim,Salim va Qobilning sevimli taomi ma\'lumoti bor')
for d in range(4):
    ism=input('kimni sevimli taomini bilmoqchisiz?\n')
    kasha=taom.get(ism)
    if kasha==None:
         print(f'Bunda {ism} ismi yo\'q')
    else:  
        print(f"{ism.title()}ning sevimli taomi {taom[ism]}")
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:39:52 2023

@author: User
"""

taom={'ali':'osh',
      'karim':'makaron',
      'salim':'shokolad',
      'qobil':'lapsha'}
#print('Bizda Ali,Karim,Salim va Qobilning sevimli taomi ma\'lumoti bor')
for d in range(4):
    ism=input('kimni sevimli taomini bilmoqchisiz?\n')
    kasha=taom.get(ism)
    if kasha==None:
         print(f'Bunda {ism} ismi yo\'q')
    else:  
        print(f"{ism.title()}ning sevimli taomi {taom[ism]}")
>>>>>>> 68ea62e24960c496529586394971374656fcbde3
       