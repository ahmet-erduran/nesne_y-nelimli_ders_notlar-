import tkinter
class OscarSinavi:
    def __init__(self):
        self.pencere = tkinter.Tk()
        self.pencere.title("Oscar Ödüllü Filmler (Dict Yöntemi)")
        
        # --- TASARIM ---
        tkinter.Label(self.pencere, text="Film Türü").grid(row=0, column=0, sticky="W")
        tkinter.Label(self.pencere, text="Film Listesi").grid(row=0, column=1, sticky="W")
        
        # Sol Kutu (Türler) - Bu sefer StringVar kullanıyoruz (Hoca gibi)
        self.degisken_turler = tkinter.StringVar() # Türleri tutacak değişken
        self.lst_turler = tkinter.Listbox(self.pencere, width=20, listvariable=self.degisken_turler)
        self.lst_turler.grid(row=1, column=0, padx=10)
        
        # Olay Bağlama
        self.lst_turler.bind('<<ListboxSelect>>', self.filmleri_getir)
        
        # Sağ Kutu (Filmler) - Bunu da StringVar ile yapabiliriz
        self.degisken_filmler = tkinter.StringVar()
        self.lst_filmler = tkinter.Listbox(self.pencere, width=30, listvariable=self.degisken_filmler)
        self.lst_filmler.grid(row=1, column=1, padx=10)
        
        # --- ÖNEMLİ KISIM: HAFIZA (SÖZLÜK) ---
        self.film_arsivi = {} # Tüm veriyi burada tutacağız!
        self.verileri_yukle() # Dosyayı oku ve sözlüğü doldur
        
        self.pencere.mainloop()

    def verileri_yukle(self):
        # Dosyayı SADECE 1 KERE okuyoruz
        dosya = open("Oscars.txt", "r", encoding="utf-8")
        
        for satir in dosya:
            parcalar = satir.strip().split(',')
            film_adi = parcalar[0].strip()
            turu = parcalar[1].strip()
            
            # --- SÖZLÜK MANTIĞI ---
            # Eğer bu tür sözlükte daha önce yoksa, boş bir liste oluştur
            if turu not in self.film_arsivi:
                self.film_arsivi[turu] = []
            
            # Sonra filmi o listenin içine at
            self.film_arsivi[turu].append(film_adi)
            
        dosya.close()
        
        # Sözlük doldu! Şimdi Türleri (Keys) alıp sol kutuya koyalım.
        # Hoca burada "tuple" kullanmıştır çünkü set() metodunda listvariable=... çalışmaz, tuple ister.
        tum_turler = sorted(list(self.film_arsivi.keys())) # Sıralı liste yaptık
        self.degisken_turler.set(tuple(tum_turler)) # Tuple'a çevirip kutuya bastık [cite: 13]

    def filmleri_getir(self, event):
        # Artık dosya okumak yok! Direkt hafızadan (sözlükten) çekiyoruz.
        
        indeks = self.lst_turler.curselection()
        if not indeks: return
        
        secilen_tur = self.lst_turler.get(indeks)
        
        # Sözlükten o türün listesini al
        filmler_listesi = self.film_arsivi[secilen_tur]
        
        # Sağ kutuya bas (Tuple'a çevirerek)
        self.degisken_filmler.set(tuple(filmler_listesi))

# Çalıştır
OscarSinavi()