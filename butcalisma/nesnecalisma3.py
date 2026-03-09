from tkinter import * # Tkinter kütüphanesini çağır

def topla():
    # 1. Kutulardaki verileri al (.get())
    # Gelen veri string (yazı) olduğu için int'e çeviriyoruz
    sayi1 = int(giris1.get())
    sayi2 = int(giris2.get())
    
    # 2. İşlemi yap
    sonuc = sayi1 + sayi2
    
    # 3. Sonucu ekrana yaz
    # Önce sonuc etiketini temizleyelim, sonra yazalım
    etiket_sonuc.config(text=f"Sonuç: {sonuc}")

# --- PENCERE AYARLARI ---
pencere = Tk()
pencere.title("Basit Hesaplayıcı")
pencere.geometry("300x200") # Pencere boyutu

# --- BİLEŞENLERİ YERLEŞTİRME (GRID SİSTEMİ) ---

# 1. Satır: Birinci Sayı
Label(pencere, text="Sayı 1:").grid(row=0, column=0, padx=10, pady=10)
giris1 = Entry(pencere)
giris1.grid(row=0, column=1)

# 2. Satır: İkinci Sayı
Label(pencere, text="Sayı 2:").grid(row=1, column=0, padx=10, pady=10)
giris2 = Entry(pencere)
giris2.grid(row=1, column=1)

# 3. Satır: Buton
# command=topla -> Butona basınca 'topla' fonksiyonuna git demek
buton = Button(pencere, text="TOPLA", command=topla)
buton.grid(row=2, column=1)

# 4. Satır: Sonuç Göstergesi
etiket_sonuc = Label(pencere, text="Sonuç: ...", font=("Arial", 12, "bold"))
etiket_sonuc.grid(row=3, column=1, pady=20)

# Pencerenin açık kalmasını sağlar (Sonsuz döngü)
pencere.mainloop()