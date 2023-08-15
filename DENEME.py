# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:57:57 2022

@author: nurhanuzun
"""

9*9
type("hello")
print("hello")
""
123
"123"
"a"+"b"
"a"  " b"
"a"+"-b"
"a"*3
"a " *3
#STRING METHODLARI -LEN
a="gelecegı_yazanlar"
gel_yaz="gelecegı_yazanlar"

a=9
b=10
a*b
# del mvk
del mvk
len(gel_yaz)
#STRING METODLARI UPPER() & LOWER()
gel_yaz="gelecegı_yazanlar"
gel_yaz.upper()
gel_yaz.lower()
gel_yaz="gelecegı_yazanlar"
b=gel_yaz.replace("e","a")
gel_yaz =" gelecegı_yazanlar "
gel_yaz.strip()  
dir(gel_yaz)
gel_yaz="gelecegı_yazanlar"
#gel_yaz.capitalize()
#gel_yaz.title()
gel_yaz[1]
gel_yaz[0:3]

#DEĞİŞKENLER
a=99999
b="ali_uzaya_git"
c=a*6

a=9
c=a*2
a/c
a*c
a*5

type(100)
type(100.2)
type(1+2j)
a=100.2
#conda create -n spyder-env spyder -y
#conda activate spyder-env
#spyder


#type dönüşümleri
birinci_sayi=input()
print("gelecegi","yazanlar")
print("gelecegi","yazanlar",sep="_")
?print


#VERİ YAPILARI
NOTLAR=[90,70,80,50]
type(NOTLAR)
liste=["a",19.3,90,NOTLAR]
type(liste[0])
liste[1]
yeni_liste=["a",10,[20,30,40,50]]
yeni_liste
yeni_liste[2]
  
liste=["ali","veli","berkcan","ayse"]
liste[1]
liste[1]="velinin_babası"
liste=liste+["kemal"]


liste=["ali","veli","berkcan","ayse"]
liste.remove("berkcan")
liste.append("kerim")
liste.insert(0,"eli")

liste.pop(4)
 liste=["ali","veli","isik","ali","veli"]
liste.count("ali")


liste_yedek=liste.copy()

liste.extend(["a","b",10])
liste.reverse()
#TUPLE OLUŞTURMA
t=("ali","veli",1,2,3.2,[5,6,7,8])

#DİCTİONARY(SÖZLÜK)

sozluk={"REG":"Regresyon Modeli",
        "LOJ":"lojistik Regresyon",
        "CART":"Classification and Reg"
        }

sozluk={"REG":10,
        "LOJ":20,
        "CART":30 }

sozluk
sozluk={"REG": ["RMSE",10],
        "LOJ": ["MSE",20],
        "CART":["SSE",30] }

sozluk["REG"]
  
sozluk= {"REG": {"RMSE":10,
                "MSE":20,
                 "SSE":30},
         
         "LOJ": {"RMSE":10,
                "MSE":20,
                "SSE":30},
         
         "CART": {"RMSE":10,
                 "MSE":20,
                 "SSE":30}}
sozluk
 sozluk["REG"]["SSE"]
#EKLEME
sozluk={"REG":"Regresyon Modeli",
        "LOJ":"lojistik Regresyon",
        "CART":"Classification and Reg"
        }
sozluk["GBM"]="Gradient Boosting Mac"
sozluk["REG"]="Coklu Dogrusal Regresyon"
sozluk
sozluk[1]="Yapay Sinir Ağları"
sozluk

l=[1]
sozluk[l]="yeni bir sey"
t=("tuple",)
sozluk[t]="yeni bir sey"
sozluk



#SETLER
#SET OLUŞTURMA
l=["a","ali",123]
 s=set(l)

t=("a","ali")
s=set(t)
ali="lutfen_ata_bakma_uzaya_git"
type(ali)
s=set(ali)
s
l=["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
s=set(l)
s
len(s)
l[0]
s[0]
 
l=["gelecegi","yazanlar"]
s=set(l)
dir(s)
s.add("ile")
s
# dasdasd
# dsasdasd
# sdasdas

set1=set([1,3,5])
set2=set([1,2,3])
set1.difference(set2)
 set2.difference(set1)
set1.symmetric_difference(set2)
set1-set2
#kesişim
set1.intersection(set2)
set1 & set2
#birleşim
set1.union(set2)
set1.intersection_update(set2)

#Set Sorgu İşlemleri
set1=set([7,8,9])
set2=set([5,6,7,8,9,10])
set1.isdisjoint(set2)
set1.issuperset(set2)

a=set([1,3,6,19])

#FONKSİYONLARA GİRİŞ VE FONKSİYON OKURYAZARLIĞI
print("a","b",sep="_")

def kare_al(x):
   print( x**2) 
    #4**2
#5**2
kare_al(5)

def kare_al(x):
    print("girilen sayının karesi:"+str(x**2))
    kare_al(3)

def kare_al(x):
    print("girilen sayı:"+str(x))
    print("girilen sayının karesi:"+str(x**2))
    kare_al(4)

def carpma(x,y):
    print(x*y)
    carpma(5,6)
      
#ısı,nem,sarj
#(40 +25)/ 90 

def direk_hesap(ısı,nem,sarj):
    print((ısı+nem)/sarj)

direk_hesap(30,60,20)
direk_hesap*9
#GELMEZ HATA VERİR
def direk_hesap(ısı,nem,sarj):
    return(ısı+nem)/sarj

direk_hesap(30,60,90)*9

x=[]
def eleman_ekle(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi")
x.append(1)
   
 eleman_ekle(1)
eleman_ekle("ali")

sınır=5000
sınır==4000

sınır=50000
gelir=40000
if gelir<sınır:
    print("gelir sınırdan küçük")

#else
if gelir>sınır:
    print("gelir sınırdan büyük")
else:
    print("gelir sınırdan küçük")

sınır=50000
gelir1=60000
gelir2=50000
gelir3=35000
if gelir1>sınır:
    print("Tebrikler hediye kazandınız.")
elif gelir<sınır:
    print ("Uyarı!")
else:
    print("Takibe devam")


if gelir2>sınır:
    print("Tebrikler hediye kazandınız.")
elif gelir2<sınır:
    print ("Uyarı!")
else:
    print("Takibe devam")


if gelir2>sınır:
    print("Tebrikler hediye kazandınız.")
elif gelir2<sınır:
    print ("Uyarı!")
else:
    print("Takibe devam")
    
 sınır=50000
 magaza_adı=input("Magaza adı nedir?")
gelir=int(input("gelirinizi giriniz:"))
if gelir>sınır:
    print ("Tebrikler,"+magaza_adı + " promosyon kazandınız!")
elif gelir< sınır :
    print ("Uyarı! Çok düşük gelir:"+str(gelir))
else:
    print("Takibe devam")

ogrencı=["ali","veli","ısık","berk"]
for i in ogrencı:
    print(i)

#FOR DÖNGÜSÜ
 maaslar=[1000,2000,3000,4000,5000,6000]
for i in maaslar :
    print(i*2)

def kare_al(x):
    print(x**2)
    kare_al(2)

maaslar=[1000,2000,3000,4000,5000]
 for i in maaslar:
     print(i)

#maaslara yuzde 20 zam yapıldı
 def yeni_maas(x):
     print(x*20/100+x)
     yeni_maas(1000)

def maas_ust(x):
    print(x*10/100+x)
def maas_alt(x):
    print(x*20/100+x)
  maaslar=[1000,2000,3000,4000,5000,6000]
for i in maaslar:
    if i >=3000:
        maas_ust(i)
    else:
        maas_alt(i)
        
maaslar=[7000,2000,3000,2000,7000,1000]
dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar:
    if i==3000:
        print("kesildi")
        break
    print(i)
    
for i in maaslar:
    if i==3000:
        print("kesildi")
        continue
    print(i)
    
sayı=1
while sayı<10:
    sayı+=1
    print(sayı)
    
class Veribilimci():
    print("Bu bir sınıftır")
    
class Veribilimci():
    bolum=''
    sql='Evet'
    deneyim_yılı=0
    bildiği_diller=[]

  ali=Veribilimci()
ali.sql
 

class Veribilimci():
    def __init__(self):
        self.bildiği_diller=[]


ali=Veribilimci()
ali.bildiği_diller


ali.bildiği_diller.append("pyhton")
ali.bildiği_diller

veli=Veribilimci()
veli.bildiği_diller

veli.bildiği_diller.append("R")
veli.bildiği_diller

 
class Employees():
    def __init__(self):
        self.FirstName=''
        self.LastName=''
        self.Address=''
        
class Datascience(Employees):
    def __init__(self):
        self.Programming=""
   
veribilimci1.Datascience()
veribilimci1.Programming()
veribilimci1.

class Marketing():
    def __init__(self):
        self.StoryTelling=""

mar1=Marketing()
mar1.StoryTelling


A=9
def impure_sum(b):
     return b+A

def pure_sum(a,b):
    return a+b

impure_sum(6)
pure_sum(3,4)

#OLUMCUL YAN ETKİLER
#açılan dosyadaki satır sayısını belirle
class LineCounter:
    def __init__(self,filename):
        self.file=open(filename,'r')
        self.lines=[]
    def read(self):
        self.lines=[line for line in self.file]
    def count(self):
        return len(self.lines)

lc=LineCounter('deneme.txt')
print(lc.lines)
print(lc.count()))
 #iç nesnenin 
print(lc.lines)
print(lc.count())
 #  FP
 def read (filename):
     with open (filename,'r') as f:
         return [line for line in f]
def count(lines):
    return len(lines)

example_lines=read('deneme.txt')
lines_count=count('deneme.txt')
lines_count


example_lines=read('deneme.txt')
lines_count=count(example_lines)
lines_count

#İsimsiz Fonksiyonlar
def old_sum(a,b):
    return a+b
old_sum(4,5)

new_sum=lambda a,b :a+b
new_sum(4,5)

sırasız_liste=[('b',3),('a',8),('d',12),('c',1)]
sırasız_liste
her bir elemanın 2. elemanına gidip sıralamak
##lambda atama işlemi yapmadan fonksıyon tanımladık sıralama işlemi yapmadık
##isimlendirme yapmadan fonksiyonu kullanıyor olmamız lambda 
sorted (sırasız_liste,key=lambda x:x[1])


#Vektörel Operasyonlar 
#↨her birini birbriyle çarpma işlemi iki vektörü 
#OOP
a=[1,2,3,4]
b=[2,3,4,5]

ab=[]
range(0,len(a))
for i in range(0,len(a)):
    print(i)
    ab.append(a[i]*b[i])
ab

#FP
#daha az kodla aynı işlemi basitleştirmek

import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

a*b


#MAP & FİLTER &REDUCE
#Her sayıya 10 eklemek 

liste=[1,2,3,4,5]
for i in liste:
    print(i+10)
 #verilen bir vektörün içerisinde belirli bir fonksiyonu çalıştırma imkanı verir
 
list(map(lambda x :x*10,liste))


#FILTER FONKSIYONU
#iteratif bir nesne alır başka bir iteratif nesne oluşturur iteratif nesne içinde aranan sartları sağlayan nesneleri filtreler

liste=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2==0,liste))

#REDUCE FONKSIYONU
#functools kütüphanesinden reduce'u çalmak
from functools import reduce
liste=[1,2,3,4]
reduce(lambda a,b:a+b,liste)

#modül oluşturma  
#HESAP MODÜLÜ MODÜLÜ 
def yeni_maas(x):
    print(x*20/100+x)

maaslar=[1000,2000,3000,5000]

#TEST MODÜLÜ
import hesap_modülü
hesap_modülü.yeni_maas(1000)

import hesap_modülü as hm
hm.yeni_maas(5000)

from hesap_modülü import yeni_maas
yeni_maas(4000)

import hesap_modülü as hm
hm.maaslar


#HATALAR/İSTİSNALAR
a=10
b=0

a/b
#ZeroDivisionError HATASI
#hata verir.
#bu kodu çalıştırmaya çalış çalışmazsa hata türünü ifade ediyoruz bir uyarı verecek
# bunu bi dene çalışmazsa hata tipi bu istisna olarak gör

try: print(a/b)
except ZeroDivisionError:
    print ("Payda da sıfır olmaz")


#TİP HATASI
#görmezden gel
a=10
b=2

a/b
try :print(a/b)
except TypeError:
    print("Sayılar sayılar ile çarpılır")


type(a)==()

pip install pandas
pip install webdriver

def calculate(varm,moisture,charge):
    return (varm+moisture)/charge
calculate(98,12,78)*10


#
def calculate(varm,moisture,charge):
    varm=varm*2
    moisture=moisture*2
    charge=charge*2
    output=(varm+moisture)/charge
    return varm,moisture,charge,output
    calculate(98,12,78)
calculate(98,12,78)
 varm,moisture,charge,output=calculate(98,12,78)
    varm,moisture,charge,output=calculate(98,12,78)

#Fonksiyon içerisinden  fonksiyon çağırmak

def calculate(varm,moisture,charge):
    return int((varm+moisture)/charge)
calculate(90,12,12)*10

def standardization(a,p):
    return a*10/100*p*p

standardization(45,1)

def  all_calculation(varm,moisture,charge,p,a):
    print(calculate(varm,moisture,charge))
    b=standardization(a, p)
    print(b*10)

all_calculation(1,3,5,12,19)


#3.2 KOŞULLAR
#TRUE FLASE
1==1
1==2
if 1==1:
    print("something") #true olursa

if 1==2:
    print("something") 
    
number=11
if number >=10 :
    print ("number is 10")

def number_check(number):
    if number ==10 :
        print ("number is 10")
 number_check(12)

#ELSE

def number_check(number):
    if number ==10 :
        print ("number is 10")
    else:
        print("number is not 10")
 number_check(10)


#FOR DÖNGÜSÜ
students=["John","Mark","Venessa","Mariam"]

students[0]

for student in students :
     print(student.upper())

salaries=[1000,2000,3000,4000,5000]

for salary in salaries :
    print(salary)

# %20 zam    
for salary in salaries :
    print(salary*20/100+salary)

#tekrar etme işlemini ortadan kaldırma 
#
def new_salary(salary,rate) :
    return int(salary*rate/100+salary)

new_salary(1500,50)


for salary in salaries:
   print( new_salary(salary, 10))


salaries2=[10700,25000,30400,40300,50200]
for salary in salaries2:
   print( new_salary(salary, 10))


#MAAŞI 3000DEN AZ OLANLARA FARKLI 3000DEN FAZLA 
#İSE FARKLI

salaries=[1000,2000,3000,4000,5000]
for salary in salaries:
    if salary>=3000:
        print( new_salary(salary, 10))
    else :
        salary<3000
        print( new_salary(salary, 20))


#MÜLAKAT SORUSU

#before: "hi my name is john and ı am learning python
#after: "Hi My NaMe İs JoHn AnD ı aM LeArNiNg pYtHoN

len("miuul")
range(len("miuul"))
range(0,5)

for i in range(0,5):
    print(i)


4%2==0



def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        #index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
         new_string += string[string_index].upper()  
         #index tek ise küçük harfe çevir.
        else : 
           new_string += string[string_index].lower()
    print(new_string)
 
alternating("kalkmak")
alternating("hi my name is john and ı am learning python")


#break koşul yakalandıysa durur.
#continue  atla devam et
#while -dığı sürece

salaries=[1000,2000,3000,4000,5000]
for salary in salaries:
    if salary==3000:
        break
    print(salary)
    

salaries=[1000,2000,3000,4000,5000]
for salary in salaries:
    if salary==3000:
        continue
    print(salary)

number=1
while number < 6:
    print(number)
    number += 1


#Enamerate :OTOMATİK COUNTER/INDEXER İLE LOOP

students=["John","Mark","Venessa","Mariam"]

for student in students:
    print(student)

for index, student in enumerate (students):
    print(index,student)

#virgül 1 dersek 1 den başlar
#tek indesklileri bir çiftleri bir

A=[]
B=[]

for index, student in enumerate (students):
   if index % 2 ==0:
       A.append(student)
   else :
        B.append(student)


#UYGULAMA 
#divide_students fonksiyonu yazın
#çift indexte yer alan öğrenciler bir listede 
#tek indexte yer alan öğrenciler başka bir listede 
#fakat bu iki liste tek bir liste olarak return olsun

students=["John","Mark","Venessa","Mariam"]
def divide_students (students):
    groups=[[],[]]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return(groups)
            
   st= divide_students(students)
st[0]


#çift indeksleri büyültsün tek indeksleri küçültsün 

def alternating_with_enumerate(string):
    new_string=""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)
    
    
alternating_with_enumerate("hi my name is john and ı am learning python")

#ZİP
#machleme eşitler birbiriyle ilişkilendirir

student=["John","Mark","Venessa","Mariam"]
departments=["mathematics","statistics","pyhsics","astronomy"]
ages=[23,30,26,22]

list(zip(students,departments,ages))

 #lambda,map,filter,reduce
 
#lambda kullan at fonk.
def summer(a,b):
    return a+b 

new_sum=lambda a,b:a+b

new_sum(4,5)


#map for döngüsünden kurtarma

salaries=[1000,2000,3000,4000,5000]

def new_salary(x):
    return x *20/100 + x
new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary,salaries))

list(map(lambda x: x*20/100 + x , salaries))
#del new_sum

list(map(lambda x: x**2, salaries))

#FILTER 
#Yçift saıları getırme
list_store=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x % 2==0,list_store ))

#REDUCE 
from functools import reduce 
list_store=[1,2,3,4]
reduce(lambda a, b : a+b, list_store)


students=["Denise","Arsen","Tony","Audrey"]
[student[0].upper() if len(student)%2!=0 else
student[0].lower() for student in students]

wages=[700,800,900,1000]
[wage*1.1 if wage>950 else wage *1.2 for wage in wages]



#PYTHON 
#ÖDEVLER
x=8 
type(x)
y=3.2
type(y)
z=8j+18
type(z)
a="Hello World"
type(a)
b=True
type(b)
c=23<22
type(c)

l=[1,2,3,4]
type(l)
#SIRALAYICIDIR.
#KAPSAYICIDIR.
#DEĞİŞTİRİLEBİLİR.

d={"Name":"Jake",
   "Age":27,
   "Adress":"Downttown"}
type(d)
# DEĞİŞTİRİLEBİLİRLER
#KAPSAYICIDIR
#SIRASIZDIR
#KEY DEĞERLERİ FARKLI OLMALI


t=("Machine Learning","Data Science")
type(t)
#SIRALIDIR 
#KAPSAYICIDR
#DEĞİŞTİRİLEMEZ.

s={"Python","Machine Learning","Data Science"}
type(s)
#DEĞİŞTİRİLEBİLİRLER.
#SIRASIZ=EŞSİZ
#KAPSAYICIDIR.


#Görev:2 bütün ifadeleri byük harf yap ve aralarında boşluk olanlar 
#space yerine virgül konmalı 
#"The goal is to turn data into information, and information into insight."
#split kelime kelime ayırır.
text="The goal is to turn data into information, and information into insight."
text.upper().replace(",",".").replace("."," ").split()



#Görev 3: ["D","A","T","A","S","C","I","E","N","C","E"]
#1. ELEMAN SAYISI
#2. SIFIRINCI VE ONUNCU İNDEKSTEKİ HARF
#3.["D","A","T","A"] ÇIKTISI
#4.Sekizinci indeksi sil
#5.Yeni bir eleman ekle
#6.Sekizinci indekse tekrar N ekle

lst=["D","A","T","A","S","C","I","E","N","C","E"]
 len(lst)
lst[0]
lst[10]

lst[0:4]

lst.pop(8)

lst.append("k")
 
lst.insert(8,"N")


#Görev 4: dict={"Christan":["America",18]
#               "Daisy"   :["England",12]
#               "Antonio" :["Spain",22]
#               "Dante"   :["Italy",25]

#1. Key değerlerine erişin 
#2. Valuelara erişin
#3.Daisy keyine ait 12 değerini 13 yap
#4.Key değeri ahmet value değeri [Turkey,24] değeri ekle
#5. Antonioyu sil 


dict={"Christan":["America",18],
      "Daisy"   :["England",12],
      "Antonio" :["Spain",22],
      "Dante"   :["Italy",25]}

dict.keys()
dict.values()
dict.update({"Daisy"  :["England",13]})

dict["Daisy"][1]=14
 
dict.update({"Ahmet"  :["Turkey",24]})

dict.pop("Antonio")


#Görev 5: Argüman listesi oluştu tek ve çift sayları ayrı ayrı listele ve 
#bu listeleri return et

l=[2,13,18,93,22]
def func(list):
    cift_list=[]
    tek_list=[]
    
    for i in list:
        if i % 2 == 0 :
            cift_list.append(i)
        else:
            tek_list.append(i)
    
    return cift_list,tek_list
cift,tek=func(l)


#Görev 6: öğrenciler=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
#Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdır.
#Mühendislik Fakültesi 1 . öğrenci:Ali
#Mühendislik Fakültesi 2 . öğrenci:Veli
#Mühendislik Fakültesi 3 . öğrenci:Ayşe
#Tıp Fakültesi 1 . öğrenci:Talat
#Tıp Fakültesi 2 . öğrenci:Zeynep
#Tıp Fakültesi 3 . öğrenci:Ece

ogrenciler=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci:",x)
    else:
        i-= 2 
        print("Tıp Fakültesi",i,". öğrenci:",x)


#Görev 7: ders_kodu=["CHP1005","PSY100","HUK1085","SEN2204"]
#kredi=[3,4,5,4]
#kontenjan=[30,75,150,25]
#zip olarak sırası ile ders kodu kredi kontenjan olarak bastırın.

ders_kodu=["CHP1005","PSY100","HUK1085","SEN2204"]
kredi=[3,4,5,4]
kontenjan=[30,75,150,25]

for ders_kodu,kredi,kontenjan in zip(ders_kodu,kredi,kontenjan):
 print(f"Kredisi {kredi }olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")



#Görev 8: kume1=set(["data","python"])
# kume2=set(["data","function","qcut","lambda","python","miuul"])
#kume 1 kume 2 yi kapsıyor ise ortak elemanlar kapsamıyor ise 2.kümenin 1.
#kümeden farkını çıkart.
#issupersek kapsamak
kume1=set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))
kume (kume1,kume2)
kume(kume2,kume1)


#COMPREHENSIONS 
#LIST COMPREHENSIONS 
#PEŞPEŞE OLAN İŞLEMLERİ LİST TİPİND ÇIKARTIR

salaries=[1000,2000,3000,4000,5000]

def new_salary(x):
    return x*20/100+x
for salary in salaries:
    print(new_salary(salary))

null_list=[]
 
for salary in salaries:
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

#tek bir satırda çözmek istersek bütün fonksiyonları peş peşe olan 
#köşeli parantez ile list formatında daha kısa şekle indirgenebilir.
[new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary*2 for salary in salaries ]

#eğer if döngüsünü  tek kullanacaksak if döngüsü sağda

[salary*2 for salary in salaries if salary <3000 ]

#eğer if döngüsünü  else ile kullanacaksak for döngüsü sağda

[salary*2  if salary <3000 else salary*0 for salary in salaries ]

[new_salary(salary*2)  if salary <3000 else new_salary(salary*0.2) for salary in salaries ]

#istemediğim öğrencilerin isimleri küçük
#diğerlerini büyük harfle düzeltmek istiyoruz
students=["John","Mark","Venessa","Mariam"]
students_no=["John","Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

[student.lower() if student  not in students_no else student.upper() for student in students]



#DICT COMPREHENSİON 
#sözlük yapılarındaki kompleksli yapıları 

dictionary={ 'a':1,
              'b':2,
              'c':3,
              'd':4}

#her bir value değerinin karesini alma
dictionary.keys()
dictionary.values()
dictionary.items()

{k:v**2 for (k,v) in dictionary.items()}

#keylere işlem yapmak istersek
{k.upper():v**2 for (k,v) in dictionary.items()}


##uUYGULAMA 
##AMAÇ ÇİFT SAYILARIN KARESİ ALINARAK BİR SÖZLÜĞE EKLENMEK 
##İSTENDİ.
##keyler orjınal değerler valuelar ise değiştirilmiş değerler

numbers=range(10)
new_dict={}
for n in numbers :
    if n % 2==0:
        new_dict[n]=n**2


{n:n**2 for n in numbers if n%2==0}


## bir veri setindeki değişken isimlerini değiştirmek

#before :
#['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses','abbrev']
#AFTER:
#['TOTAL','SPEEDİNG','ALCOHOL','NOT_DISTRACTED','NO_PREVIOUS','INS_PREMIUM','INS_LOSSES','ABBREV']

#kütüphane 
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.lower())
    
#kalıcı olması için

A=[]
for col in df.columns:
    A.append(col.upper())
    
df.columns=A


df=sns.load_dataset("car_crashes")
df.columns=[col.upper() for col in df.columns]

#ISMINDE "INS" OLAN DEĞİŞKENLERİN BAŞINA FLAG 
#DİĞERLERİNE NO_FLAG_ EKLEMEK İSTİYORUZ.

#BEFORE
#['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

#AFTER
#['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDING',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DISTRACTED',
# 'NO_FLAG_NO_PREVIOUS',
# 'FLAG_INS_PREMIUM',
# 'FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV']


[col for col in df.columns if "INS" in col]

["FLAG_"+col for col in df.columns if "INS" in col]


["FLAG_"+col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]

df_columns=["FLAG_"+col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]



#sadece sayısal değişkenler
##{'total' : ['mean','min','max','var'],
#  'speeding' :['mean','min','max','var'],
#  'alcohol' :['mean','min','max','var'],
#  'not_distracted':['mean','min','max','var'],
#  'no_previous' :['mean','min','max','var'],
#  'ins_premium':['mean','min','max','var'],
#  'ins_losses':['mean','min','max','var'],
#  'abbrev':['mean','min','max','var'],}


import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
#sayısal değişkenleri seçtik
# o ifadesi kategorik olduğunu ifade eder numeric olsun istediğimiz için sadece nümerik
num_cols=[col for col in df.columns if df[col].dtype!="O"]
soz={}
agg_list=['mean','min','max','var']

#sol taraf dinamikken sağ taaraf sbit
for col in num_cols:
    soz[col]=agg_list
    

#kısa yolu

new_dict={col:agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)


#sorular
names=["denise","jean","fleur"]
ages=[20,32,45]
cities=["lyon","lille","nantes"]
list(zip(names,ages,cities))

wages=[1000,2000,3000,4000,5000]
new_wages=lambda x: x*0.20+x
list(map(new_wages,wages))

students=["Denise","Arsen","Tony","Audrey"]

low=lambda x: x[0].lower()
print(list(map(low,students)))

dictn={"Denise":10,
       "Arsen":12 }

new_dict={k:v+3 for (k,v) in dictn.items()}









































































































