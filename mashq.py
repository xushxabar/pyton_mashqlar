#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars=['toyota','mazda','hyundai','gm','kia']
for c in cars:
    if c.upper()!='GM': print(c.title())
    else: print(c.upper())
    
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
admin = "Gayrat"
ism=input('Ismingizni kiriting:\n>>>')
if ism.lower() == admin.lower():
    print("Hush kelibsiz, Admin. Foydalanuvchilar ro\'yhatini ko\'rasizmi?")
else: print("Hush kelibsiz, ",ism.title()) 

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng
#bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
s1=int(input("Assalomu alaykum, 2ta son kiriting:\nBirinchi son:"))
s2=int(input("Ikkinchi son: "))
if s1==s2:print('Sonlar teng')
else: print('Sonlar teng emas')

#son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", 
#agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
s= int(input('Istalgan son kiriting: \n>>>'))
if s>=0 : print('Bu son musbat')
else: print('Bu son manfiy')

#son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
#Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
s=int(input('Musbat son kiriting:\n>>>'))
if s>=0:print('Bu sonning ildizi ',s**(1/2),'ga teng')
else: print('Musbat son kiriting') 
    