import tkinter as tk


class GrafikCizici:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Not Grafiği")

        # Veriler (Sınav notları gibi düşün)
        self.notlar = [40, 80, 20, 100, 60]

        # Tuval Boyutları
        cw = 400  # Canvas Width
        ch = 200  # Canvas Height

        self.tuval = tk.Canvas(self.pencere, width=cw, height=ch, bg="white")
        self.tuval.pack()

        # --- ÇİZİM ALGORİTMASI ---

        bar_genisligi = 40
        bosluk = 20
        x_baslangic = 30  # İlk sütun nereden başlasın

        for i in range(len(self.notlar)):
            puan = self.notlar[i]

            # KOORDİNAT HESABI (En önemli kısım)
            # Sol kenar: Başlangıç + (Sıra * (Genişlik + Boşluk))
            x1 = x_baslangic + (i * (bar_genisligi + bosluk))

            # Sağ kenar: Sol kenar + Genişlik
            x2 = x1 + bar_genisligi

            # Alt kenar: Tuvalin en dibi (200)
            y2 = ch

            # Üst kenar: Dip - Puan (Ters Y ekseni!)
            # 100 puanlık yer kaplasın istiyorsak 200'den 100 yukarı çıkmalıyız.
            y1 = ch - puan

            # Rengi puana göre ayarlayalım (Bonus)
            renk = "red" if puan < 50 else "green"

            # Kutuyu Çiz
            self.tuval.create_rectangle(x1, y1, x2, y2, fill=renk)

            # Puanı üstüne yaz
            self.tuval.create_text(x1 + 20, y1 - 10, text=str(puan), fill="black")

        self.pencere.mainloop()


GrafikCizici()
