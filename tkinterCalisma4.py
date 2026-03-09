import tkinter


class SenatorSistemi:
    def __init__(self):
        self.pencere = tkinter.Tk()
        self.pencere.title("Eyalet Seç - Senatör Gör")

        # --- SOL TARAFI KURUYORUZ (EYALETLER) ---
        tkinter.Label(self.pencere, text="EYALETLER").grid(row=0, column=0)

        # exportselection=False: Sağ tarafa tıklayınca buradaki mavi seçim sönmesin diye.
        self.liste_eyalet = tkinter.Listbox(self.pencere, exportselection=False)
        self.liste_eyalet.grid(row=1, column=0, padx=10, pady=10)

        # 'bind': "Bu listeye tıklandığında (Select) 'eyalet_secildi' fonksiyonuna git" emri.
        self.liste_eyalet.bind("<<ListboxSelect>>", self.eyalet_secildi)

        # --- SAĞ TARAFI KURUYORUZ (SENATÖRLER) ---
        tkinter.Label(self.pencere, text="SENATÖRLER").grid(row=0, column=1)

        self.liste_senator = tkinter.Listbox(
            self.pencere, width=30, exportselection=False
        )
        self.liste_senator.grid(row=1, column=1, padx=10, pady=10)

        # --- BAŞLANGIÇ: EYALETLERİ YÜKLE ---
        self.eyaletleri_yukle()

        self.pencere.mainloop()

    def eyaletleri_yukle(self):
        # Dosyayı okuyup BENZERSİZ eyaletleri bulmamız lazım.
        # Küme (set) kullanıyoruz çünkü kümeler aynı elemandan 2 tane barındırmaz.
        benzersiz_eyaletler = set()

        dosya = open("EyaletSenator.txt", "r", encoding="utf-8")
        for satir in dosya:
            # Satır: "Richard Shelby, Alabama, R"
            parcalar = satir.strip().split(",")
            eyalet = parcalar[1].strip()  # "Alabama"yı aldık
            benzersiz_eyaletler.add(eyalet)  # Kümeye attık
        dosya.close()

        # Kümeyi listeye çevirip sıralayalım (A'dan Z'ye düzgün dursun)
        sirali_eyaletler = sorted(list(benzersiz_eyaletler))

        # Sol kutuya doldur
        for e in sirali_eyaletler:
            self.liste_eyalet.insert(tkinter.END, e)

    def eyalet_secildi(self, event):
        # 1. Sağ tarafı temizle (Eski senatörler gitsin)
        self.liste_senator.delete(0, tkinter.END)

        # 2. Soldan seçileni al (Güvenlik kilidiyle beraber)
        indeks = self.liste_eyalet.curselection()
        secilen_eyalet = self.liste_eyalet.get(indeks)

        # 3. Dosyayı tekrar açıp o eyaletteki adamları bul
        dosya = open("EyaletSenator.txt", "r", encoding="utf-8")
        for satir in dosya:
            parcalar = satir.strip().split(",")

            isim = parcalar[0].strip()  # "Richard Shelby"
            eyalet = parcalar[1].strip()  # "Alabama"
            parti = parcalar[2].strip()  # "R"

            # EĞER dosyadaki eyalet == Tıklanan eyalet ise:
            if eyalet == secilen_eyalet:
                # Sağ kutuya ekle
                self.liste_senator.insert(tkinter.END, f"{isim} ({parti})")

        dosya.close()


# Başlat
SenatorSistemi()
