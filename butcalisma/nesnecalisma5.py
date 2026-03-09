import tkinter as tk
import pickle


def uygulama_baslat():
    pencere = tk.Tk()
    pencere.title("Sınıfsız Not Sistemi")
    pencere.geometry("450x350")

    # --- FONKSİYONLAR (Main'in içinde tanımlıyoruz ki kutulara erişebilsin) ---

    def kaydet():
        # 1. Verileri kutulardan al
        ad = giris_ad.get()
        notu = giris_not.get()

        # 2. CLASS YERİNE SÖZLÜK YAPIYORUZ
        yeni_kayit = {"isim": ad, "puan": notu}

        # 3. Önce eski listeyi dosyadan çekelim (Silinmesin diye)
        tum_liste = []

        with open("notlar_v2.dat", "rb") as dosya:
            # Tek seferde tüm listeyi çekiyoruz (while döngüsüne gerek yok)
            tum_liste = pickle.load(dosya)

        # 4. Yeni kaydı listeye ekle
        tum_liste.append(yeni_kayit)

        # 5. Güncel listeyi KOMPLE dosyaya yaz (wb: Üzerine Yazma Modu)
        with open("notlar_v2.dat", "wb") as dosya:
            pickle.dump(tum_liste, dosya)

        lbl_durum.config(text=f"{ad} başarıyla eklendi.", fg="green")

        # Kutuları temizle
        giris_ad.delete(0, tk.END)
        giris_not.delete(0, tk.END)

    def listele():
        liste_kutusu.delete(0, tk.END)  # Ekranı temizle

        dosya = open("notlar_v2.dat", "rb")
        # TEK SATIRDA OKUMA (Çünkü içeride tek bir liste var)
        gelen_liste = pickle.load(dosya)

        # Listenin içindeki sözlükleri dön
        for ogr in gelen_liste:
            # Sözlük olduğu için ['isim'] şeklinde ulaşıyoruz
            formatli_yazi = f"{ogr['isim']} -- Notu: {ogr['puan']}"
            liste_kutusu.insert(tk.END, formatli_yazi)

        lbl_durum.config(text="Liste güncellendi.", fg="blue")

    # --- ARAYÜZ TASARIMI ---

    tk.Label(pencere, text="Öğrenci Adı:").pack(pady=5)
    giris_ad = tk.Entry(pencere)
    giris_ad.pack()

    tk.Label(pencere, text="Sınav Notu:").pack(pady=5)
    giris_not = tk.Entry(pencere)
    giris_not.pack()

    btn_kaydet = tk.Button(pencere, text="Kaydet", command=kaydet)
    btn_kaydet.pack(pady=10)

    btn_listele = tk.Button(pencere, text="Listele", command=listele)
    btn_listele.pack()

    lbl_durum = tk.Label(pencere, text="...")
    lbl_durum.pack(pady=5)

    tk.Label(pencere, text="--- LİSTE ---").pack()
    liste_kutusu = tk.Listbox(pencere, width=40)
    liste_kutusu.pack(pady=10)

    pencere.mainloop()


# Programı çalıştır
if __name__ == "__main__":
    uygulama_baslat()
