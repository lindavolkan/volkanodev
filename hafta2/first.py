#Görev 1:Verilen değerlerin veri yapılarını inceleyiniz

#A
x=8
print(type(x))

#B
y=3.2
print(type(y))

#C
z=8j +18
print(type(z))

#D
a="Hello World"
print(type(a))

#E
b =True
print(type(b))

#F
c =23<22
print(type(c))

#G
l =[1,2,3]
print(type(l))

#H
d = {"Name":"Jake",
     "Age": 27,
     "Adress": "Downtown"}
print(type(d))

#I
t = ("Machine Learning", "Data Science")
print(type(t))

#J
s = {"Python", "Machine Learning", "Data Science"}
print(type(s))



#Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.Virgül ve nokta yerine space koyunuz,kelime kelime ayırınız.

text ="The goal is to turn data into information,and information into insight."
#Tüm harfleri büyük harfe dönüştürme
text =text.upper()
#Virgül ve noktayı space(boşluk) ile değiştirme
text =text.replace(',','').replace('.','')
#kelime kelime ayırma
kelime=text.split()
print(kelime)


#Görev 3:Verilen listeye aşağıdaki adımları uygulayınız.

v=["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
#Verilen listenin eleman sayısına bakınız
eleman_sayısı = len(v)
print("Listenin eleman sayısı:", eleman_sayısı)

#Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
sıfırıncı_indeks =v[0]
onuncu_indeks =v[10]
print("Sıfırıncı indeksteki eleman:" ,sıfırıncı_indeks)
print("Onuncu indeksteki eleman:" , onuncu_indeks)

#Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
alt_liste =v[0:4]
print("Oluşturulan alt liste:",alt_liste)

#Sekizinci indeksteki elemanı siliniz.
del v[8]
print("Sekizinci eleman silindikten sonra oluşan liste:", v)

#Yeni bir eleman ekleyiniz.
v.append("x")
print("Yeni eleman eklendikten sonra oluşan liste:", v)

#Sekizinci indekse "N" elemanını tekrar ekleyiniz.
v.insert(8,"N")
print("Sekizinci indekse 'N' eklendikten sonra oluşan liste:", v)

#Görev 4:Verilen sözcük yapısına aşağıdaki adımları uygulayınız.
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

#Key değerlerine erişiniz.
keys =dict.keys()
print(keys)
#Value değerlerine erişiniz.
value =dict.values()
print(value)
#Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict['Daisy'][1] =13
print(dict)
#Key değeri Ahmet value değeri [Turkey,24]olan yeni bir değer ekleyiniz.
dict['Ahmet']=["Turkey",24]
print(dict)
#Antonio'yu dictionary'den siliniz
del dict['Antonio']
print(dict)


#Görev 5:Argüman olarak bir liste olan,listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2,13,18,93,22]
def tek_çift_ayır(l):
    tek_sayılar = []
    çift_sayılar =[]

    for sayı in l:
        if sayı %2==0:
            çift_sayılar.append(sayı)
        else:
            tek_sayılar.append(sayı)
    return tek_sayılar, çift_sayılar
tekler,çiftler = tek_çift_ayır(l)
print("Tek sayılar:", tekler)
print("Çift sayılar:" ,çiftler)

#Görev 6:Enumerate Kullanımı

öğrenciler =["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
print("Mühendislik Fakültesi Başarı Sıralaması:")
for derece,öğrenci in enumerate(öğrenciler[:3],1):
    print(f"{öğrenci}: {derece}.derece")
    print("Tıp Fakültesi Başarı Sıralaması:")
for derece, öğrenci in enumerate(öğrenciler[3:], 1):
        print(f"{öğrenci}: {derece}.derece")

#Görev 7:Zip Kullanımı
ders_kodu =["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi =[3,4,2,4]
kontenjan =[30,75,150,25]
for kod, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi {} olan {} kodlu dersin kontenjanı {} kişidir.".format(kredi, kod, kontenjan))

#Görev 8:Set
kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])
birleşim = kume1.union(kume2)
print("Birleşim:",birleşim)
kesişim = kume1.intersection(kume2)
print("Kesişim:", kesişim)
fark = kume2.difference(kume1)
print("Fark:", fark)
sonuç= kume2.issuperset(kume1)
print("kume2, kume1'in süper kümesi mi?:" , sonuç)


#LIST COMPREHENSION
#Görev 1:
import seaborn as sns
df =sns.load_dataset("car_crashes")
numeric_columns = df.select_dtypes(include="number").columns
new_column_names= {col:f"NUM_{col.upper()}" for col in numeric_columns}
df.rename(columns=new_column_names, inplace=True)
print(df.columns)

#Görev 2:
import seaborn as sns
df =sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]
df.columns = [f"{col}_FLAG" if "NO" not in col else col for col in df.columns]
print(df.columns)

#Görev 3:
import seaborn as sns
df =sns.load_dataset("car_crashes")
print(df.head())

import seaborn as sns
df =sns.load_dataset("car_crashes")
reference_names = [col.upper() for col in df.columns if "NO" in col.upper()]
all_column_names = [col.upper() for col in df.columns]
different_names = [col for col in all_column_names if col not in reference_names]
new_df= df[different_names]
print(new_df.columns)











