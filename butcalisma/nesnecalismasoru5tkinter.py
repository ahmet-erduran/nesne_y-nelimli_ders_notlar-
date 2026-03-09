import tkinter

def main():
    pencere = tkinter.Tk()
    pencere.title("Giriş Ekranı")
    pencere.geometry("200x150") 

    # --- ARAYÜZ ELEMANLARI ---
    
    # 1. Etiketler
    tkinter.Label(pencere, text="Kullanıcı Adı: ").grid(row=0, column=0)
    tkinter.Label(pencere, text="Şifre: ").grid(row=1, column=0)

    # 2. Giriş Kutuları (DİKKAT: .grid'i alt satırda yapıyoruz!)
    kullaniciAdi = tkinter.Entry(pencere)
    kullaniciAdi.grid(row=0, column=1)

    sifre = tkinter.Entry(pencere, show="*") # Şifreyi yıldızlı gösterir
    sifre.grid(row=1, column=1)

    # 3. Sonuç Etiketi (Başta boş, sonra değiştireceğiz)
    # Bunu fonksiyonun içinde değil burada tanımlıyoruz ki her seferinde yeni etiket oluşturmayalım.
    sonuc_etiketi = tkinter.Label(pencere, text="")
    sonuc_etiketi.grid(row=3, column=1)

    # --- KONTROL FONKSİYONU ---
    # Bu fonksiyonu main'in içine yazdık ki 'sifre' ve 'sonuc_etiketi' değişkenlerini görebilsin.
    def giris_kontrol():
        girilen_sifre = sifre.get() # .get() parantezli olmalı!
        
        # Giriş kutusundan gelen veri her zaman STRING'dir. Tırnak içinde "1234" ile kıyasla.
        if girilen_sifre == "1234":
            # Etiketin içeriğini .config ile güncelliyoruz
            sonuc_etiketi.config(text="Giriş Başarılı", fg="green")
        else:
            sonuc_etiketi.config(text="Hatalı Şifre", fg="red")

    # 4. Buton
    # command=giris_kontrol -> Parantez koymadan sadece fonksiyon ismini yazıyoruz!
    tkinter.Button(pencere, text="Giriş Yap", command=giris_kontrol).grid(row=2, column=1, pady=5)

    pencere.mainloop()

if __name__ == "__main__":
    main()