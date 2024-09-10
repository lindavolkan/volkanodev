# ÖDEV
### Virtual Environment Oluşturma ###

## ödev1:Kendi isminizde bir virtual environment oluşturunuz.Oluşturma esnasında python 3 kurulumu yapınız.##

##Cevap##    conda create -n volcano
             #conda install python 3

## ödev2:Oluşturduğunuz environment'ı aktif ediniz.##

##Cevap##    conda activate volcano

## ödev3:Yüklü paketleri listeleyiniz.##

##Cevap##     conda list

## ödev4:Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.##

##Cevap##     conda install Numpy Pandas=1.2.1
              # #we have to install python=3.7 ##

## ödev5:İndirilen Numpy'ın versiyonu nedir?##

##Cevap##     conda list (version==Numpy 1.21.5)

## ödev6:Pandas'ı upgrade ediniz.##

##Cevap##     conda upgrade pandas

## ödev7:Numpy'ı environmentten siliniz.##

##Cevap##     conda remove numpy

## ödev8:Seaborn ve Matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.##

##Cevap##      conda install seaborn matplotlib

## ödev9:Virtual environment içindeki kütüphaneleri versiyon bilgisi ile birlikte export ediniz ve yaml dosyasını inceleyiniz.##

##Cevap##      conda env export > environment.yaml

## ödev10:Oluşturduğunuz environment'ı siliniz.Önce environment'ı deaktif ediniz.##

##Cevap##      conda deactivate
               #conda env remove -n volcano