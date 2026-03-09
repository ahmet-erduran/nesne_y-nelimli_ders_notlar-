import pickle
from tkinter import *

"""
////////////////////////////////////////////////////////////////////////
veriler=["ahmet","can",{1:2,2:"ahmet"}]
dosya = open("verilerim.dat","wb")
pickle.dump(veriler,dosya)
dosya.close
///////////////////////////////////////////////////////////////////////
dosya = open("verilerim.dat","rb")
gelen_veri=pickle.load(dosya)
dosya.close

print(gelen_veri)
//////////////////////////////////////////////////////////

class Ogrenci:

    def __init__ (self,gelen_isim,gelen_numara):

        self.ad=gelen_isim
        self.numara=gelen_numara

    def bilgi_ver(self):
        print(f"Benim adım {self.ad}, Numaram {self.numara}")

ogr1=Ogrenci("Ahmet",123)
ogr2=Ogrenci("mehmet",1234)

ogr1.bilgi_ver()
ogr2.bilgi_ver()
////////////////////////////////////////////////////////////////////
"""

"""
etiket=Label(ekran,text="Adiniz: ", font=("Arial" ,8))
etiket.grid(row=0,column=0)

kutu=Entry(ekran)
kutu.grid(row=0,column=1)
#gelen_veri=kutu.get()
#kutu.delete(0,tkinter.END)

buton=Button(ekran,text="kaydet",command="kaydet")
buton.grid(row=1,column=1)

yazi_degiskeni = StringVar()

yazi_degiskeni.set("Merhaba")

kutu=Entry(ekran,textvariable=yazi_degiskeni)
kutu.pack

"""
import tkinter
import pickle


# --- 1. BÖLÜM: KALIP (CLASS) ---
# Öğrenci bilgilerini paketlemek için bu kalıbı kullanacağız.
class Ogrenci:
    def __init__(self, ad, not_degeri):
        self.ad = ad
        self.not_degeri = not_degeri

    # Listbox'ta güzel görünmesi için bu özel fonksiyonu ekliyoruz
    def __str__(self):
        return f"{self.ad} -- Notu: {self.not_degeri}"


# --- 2. BÖLÜM: ARAYÜZ VE İŞLEMLER ---
class NotSistemi:
    def __init__(self):
        self.pencere = tkinter.Tk()
        self.pencere.title("Final Hazırlık: Not Sistemi")
        self.pencere.geometry("500x300")

        # --- SOL TARAF (GİRİŞLER) ---
        # Adı Giriş
        tkinter.Label(self.pencere, text="Öğrenci Adı:").grid(
            row=0, column=0, sticky="E", padx=10, pady=10
        )
        self.giris_ad = tkinter.Entry(self.pencere)
        self.giris_ad.grid(row=0, column=1)

        # Not Giriş
        tkinter.Label(self.pencere, text="Sınav Notu:").grid(
            row=1, column=0, sticky="E", padx=10, pady=10
        )
        self.giris_not = tkinter.Entry(self.pencere)
        self.giris_not.grid(row=1, column=1)

        # --- ORTA (BUTONLAR) ---
        # Kaydet Butonu
        btn_kaydet = tkinter.Button(
            self.pencere, text="Dosyaya Kaydet (Pickle)", command=self.kaydet
        )
        btn_kaydet.grid(row=2, column=0, columnspan=2, pady=10)

        # Listele Butonu
        btn_listele = tkinter.Button(
            self.pencere, text="Listeyi Getir", command=self.listele
        )
        btn_listele.grid(row=3, column=0, columnspan=2)

        # Durum Mesajı (Label) - Kullanıcıya bilgi vermek için
        self.lbl_mesaj = tkinter.Label(self.pencere, text="Hazır", fg="blue")
        self.lbl_mesaj.grid(row=4, column=0, columnspan=2, pady=10)

        # --- SAĞ TARAF (LİSTE) ---
        tkinter.Label(self.pencere, text="Kayıtlı Öğrenciler").grid(row=0, column=2)

        self.liste_kutusu = tkinter.Listbox(self.pencere, width=30, height=15)
        self.liste_kutusu.grid(row=1, column=2, rowspan=4, padx=20)

        # Program kapanmasın diye mainloop
        self.pencere.mainloop()

    # --- 3. BÖLÜM: FONKSİYONLAR ---

    def kaydet(self):
        # 1. Kutulardaki veriyi al
        ad = self.giris_ad.get()
        notu = self.giris_not.get()

        # 2. Class (Sınıf) kullanarak nesneye çevir
        yeni_ogrenci = Ogrenci(ad, notu)

        # 3. Önce mevcut dosyayı oku (Eski kayıtlar silinmesin diye)
        try:
            dosya_oku = open("notlar.dat", "rb")
            tum_ogrenciler = pickle.load(dosya_oku)
            dosya_oku.close()
        except:
            tum_ogrenciler = []  # Dosya yoksa boş liste ile başla

        # 4. Yeni öğrenciyi listeye ekle
        tum_ogrenciler.append(yeni_ogrenci)

        # 5. Güncel listeyi tekrar Pickle ile kaydet (Dump)
        dosya_yaz = open("notlar.dat", "wb")
        pickle.dump(tum_ogrenciler, dosya_yaz)
        dosya_yaz.close()

        self.lbl_mesaj.config(text=f"{ad} kaydedildi!", fg="green")

        # Kutuları temizle
        self.giris_ad.delete(0, tkinter.END)
        self.giris_not.delete(0, tkinter.END)

    def listele(self):
        # Listbox'ı temizle
        self.liste_kutusu.delete(0, tkinter.END)

        try:
            # 1. Dosyayı aç ve oku (Load)
            dosya = open("notlar.dat", "rb")
            gelen_liste = pickle.load(dosya)
            dosya.close()

            # 2. Listbox'a tek tek ekle
            for ogr in gelen_liste:
                # ogr bir NESNE'dir. String'e çevirip ekliyoruz.
                self.liste_kutusu.insert(tkinter.END, str(ogr))

            self.lbl_mesaj.config(text="Liste güncellendi.", fg="blue")

        except:
            self.lbl_mesaj.config(text="Henüz hiç kayıt yok!", fg="red")


# Programı Başlat
NotSistemi()

""""""
