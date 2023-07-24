# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 19:42:59 2023

@author: User
"""

cars=['bmw', 'malibu', 'volvo', 'mersedes', 'mers']
print(cars)
dav=['ozbek','qozoq','tojik','turkman','afgon','tatar','ingliz','german','shved','portugal','rasha']
print(len(dav))
dav.sort()
print(dav)
#['afgon', 'german', 'ingliz', 'ozbek', 'portugal', 'qozoq', 'rasha', 'shved', 'tatar', 'tojik', 'turkman']
print(sorted(dav))
#['afgon', 'german', 'ingliz', 'ozbek', 'portugal', 'qozoq', 'rasha', 'shved', 'tatar', 'tojik', 'turkman']
print(sorted(dav,reverse=True))
print(dav)
#Asl ro'yhat o'zgarmadi---
#['turkman', 'tojik', 'tatar', 'shved', 'rasha', 'qozoq', 'portugal', 'ozbek', 'ingliz', 'german', 'afgon']
#['afgon', 'german', 'ingliz', 'ozbek', 'portugal', 'qozoq', 'rasha', 'shved', 'tatar', 'tojik', 'turkman']
dav.sort(reverse=True)
print(dav)
#sonlar
sonlar=list(range(120,1200,120))
print(sonlar)
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
