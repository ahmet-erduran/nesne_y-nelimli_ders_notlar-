import tkinter as tk
import pickle

# Hafızadaki veriler
ogrenci_listesi = [] 

def kaydet():
    ad = ent_ad.get()
    puan = ent_not.get()   
    kisi = {"isim": ad, "puan": puan}    
    # Dosyaya ekle
    with open("notlar.dat", "ab") as f:
        pickle.dump(kisi, f)   
    # Listbox'a ve hafızaya da ekle (Dosyayı tekrar okumaya gerek kalmasın)
    liste.insert(tk.END, ad)
    ogrenci_listesi.append(kisi)   
    # Temizle
    ent_ad.delete(0, tk.END)
    ent_not.delete(0, tk.END)


def notu_goster(event):
    # Tıklanan kaçıncı sırada?
    secilen = liste.curselection()   
    indeks = secilen[0] # Örn: 2 (3. sıradaki öğrenci)       
    # Hafızadaki listeden o sıradaki sözlüğü çek
    secilen_ogrenci = ogrenci_listesi[indeks]       
    # Ekrana bas
    lbl_sonuc.config(text=f"Notu: {secilen_ogrenci['puan']}", fg="red", font=("Arial", 14))

pencere = tk.Tk()
pencere.title("Örnek 5 - Pickle Detay")

# Giriş Kısmı
tk.Label(pencere, text="Ad:").grid(row=0, column=0)
ent_ad = tk.Entry(pencere)
ent_ad.grid(row=0, column=1)

tk.Label(pencere, text="Not:").grid(row=1, column=0)
ent_not = tk.Entry(pencere)
ent_not.grid(row=1, column=1)

tk.Button(pencere, text="Kaydet", command=kaydet).grid(row=2, column=0, columnspan=2)

# Liste ve Detay
liste = tk.Listbox(pencere)
liste.grid(row=3, column=0, columnspan=2, pady=10)
liste.bind("<<ListboxSelect>>", notu_goster)

lbl_sonuc = tk.Label(pencere, text="Notu: ...")
lbl_sonuc.grid(row=4, column=0, columnspan=2)

pencere.mainloop()