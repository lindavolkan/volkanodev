###Görev 1:  Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import seaborn as sns
titanic = sns.load_dataset("titanic")
print(titanic.head())
print(titanic.info())

###Görev 2:  Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.


gender_counts = titanic['sex'].value_counts()
print(gender_counts)

# Görev 3:  Her bir sutuna ait unique değerlerin sayısını bulunuz.


unique_counts = titanic.nunique()
print(unique_counts)

# Görev 4:  pclass değişkenini nunique değerlerinin sayısını bulunuz.


pclass_unique_count = titanic['pclass'].nunique()
print(pclass_unique_count)

# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.


pclass_unique_count = titanic['pclass'].nunique()
parch_unique_count = titanic ['parch'].nunique()
print(f"pclass unique değer sayısı: {pclass_unique_count}")
print(f"parch unique değer sayısı. {parch_unique_count}")


# Görev 6:  embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

print("Embarked değişkeninin tipi (önce):", titanic['embarked'].dtype)
titanic['embarked'] = titanic['embarked'].astype('category')
print("Embarked değişkeninin tipi (sonra):", titanic['embarked'].dtype)


# Görev 7:  embarked değeri C olanların tüm bilgilerini gösteriniz.

embarked_c_passengers = titanic.loc[titanic['embarked'] == 'C']
print(embarked_c_passengers)

# Görev 8:  embarked değeri S olmayanların tüm bilgilerini gösteriniz.

non_s_embarked_passengers = titanic.loc[titanic['embarked'] != 'S']
print(non_s_embarked_passengers)


# Görev 9:   Yaşı 30'dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

young_female_passengers = titanic.loc[(titanic['age'] < 30) & (titanic['sex'] == 'female')]
print(young_female_passengers)

# Görev 10:  Fare'i 500'den büyük veya yaşı 70'den büyük yolcuların bilgilerini gösteriniz.

high_fare_or_old_passengers = titanic.loc[(titanic['fare'] > 500 ) | (titanic['age'] > 70)]
print(high_fare_or_old_passengers)

# Görev 11:  Her bir değişkendeki boş değerlerin toplamını bulunuz.

missing_values = titanic.isna().sum()
print(missing_values)

# Görev 12:  who değişkenini dataframe’den çıkarınız.

titanic = titanic.drop(columns=['who'])
print(titanic.head())

# Görev 13:  deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri(mode) ile doldurunuz.

mode_deck =titanic['deck'].mode()[0]
titanic['deck'] = titanic['deck'].fillna(mode_deck)
print(titanic.head())

# Görev 14:  age değişkenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

median_age = titanic['age'].median()
titanic['age'] = titanic['age'].fillna(median_age)
print(titanic.head())

# Görev 15:  survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.


grouped_stats = titanic.groupby(['pclass' ,'sex'])['survived'].agg(['sum','count','mean'])
print(grouped_stats)


# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz. (apply ve lambda yapıların ıkullanınız)

def age_flag_function(age):
    return 1 if age < 30 else 0
titanic['age_flag'] = titanic['age'].apply(lambda x: age_flag_function(x))
print(titanic.head())

# Görev 17:  Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

import seaborn as sns
tips = sns.load_dataset("tips")
print(tips.head())
print(tips.info())

# Görev 18:  Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

summary_stats = tips.groupby('time')['total_bill'].agg(['sum','min','max','mean'])
print(summary_stats)

# Görev 19:  Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

summary_stats = tips.groupby(['day','time'])['total_bill'].agg(['sum','min','max','mean'])
print(summary_stats)

# Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

filtered_data = tips[(tips['time'] == 'Lunch') & (tips['sex'] == 'Female')]
summary_stats = filtered_data.groupby('day')[['total_bill','tip']].agg(['sum','min','max','mean'])
print(summary_stats)

# Görev 21:size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

filtered_orders = tips.loc[(tips['size'] < 3) & (tips['total_bill'] > 10)]
mean_values = filtered_orders [['total_bill','tip']].mean()
print(mean_values)


# Görev 22:  total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

tips = tips.assign(total_bill_tip_sum=tips['total_bill'] + tips['tip'])
print(tips.head())


# Görev 23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

tips = tips.assign(total_bill_tip_sum=tips['total_bill'] + tips['tip'])
top_30 = tips.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
print(top_30)


