import tkinter as tk


class SecimGrafigi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Seçim Grafiği")

        # 1. Buton
        btn = tk.Button(self.pencere, text="Grafiği Çiz", command=self.ciz)
        btn.pack(pady=10)

        # 2. Tuval (Canvas) - Arkaplan beyaz
        # Genişlik: 400, Yükseklik: 300
        self.tuval = tk.Canvas(self.pencere, width=400, height=300, bg="white")
        self.tuval.pack()

        self.pencere.mainloop()

    def ciz(self):
        self.tuval.delete("all")  # Önce ekranı temizle (Eski çizimler gitsin)

        # Başlangıç X konumu (İlk sütun soldan 20px içeride başlasın)
        x_baslangic = 20

        try:
            with open("secim.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    # Satır: "A Partisi,150" -> Parçala
                    parcalar = satir.strip().split(",")
                    parti_adi = parcalar[0]
                    oy_sayisi = int(parcalar[1])  # Matematik için INT şart!

                    # --- KOORDİNAT HESABI (En Önemli Kısım) ---

                    # Sütun Genişliği: 50px olsun.
                    # x1: Sütunun sol kenarı
                    # x2: Sütunun sağ kenarı (sol + 50)
                    x1 = x_baslangic
                    x2 = x_baslangic + 50

                    # y1: Tavan (300'den oyu çıkarıyoruz çünkü Y ters işler!)
                    # y2: Taban (Canvas'ın en altı yani 300)
                    y1 = 300 - oy_sayisi
                    y2 = 300

                    # 1. Kutuyu Çiz (Mavi renkli)
                    self.tuval.create_rectangle(x1, y1, x2, y2, fill="blue")

                    # 2. Üstüne Oy Sayısını Yaz
                    self.tuval.create_text(x1 + 25, y1 - 10, text=str(oy_sayisi))

                    # 3. Altına Parti Adını Yaz
                    self.tuval.create_text(
                        x1 + 25, y2 + 15, text=parti_adi, font=("Arial", 8)
                    )

                    # --- SONRAKİ SÜTUN İÇİN HAZIRLIK ---
                    # X konumunu 80 birim sağa kaydır (50 sütun + 30 boşluk)
                    x_baslangic += 80

        except FileNotFoundError:
            print("Dosya bulunamadı!")


SecimGrafigi()
