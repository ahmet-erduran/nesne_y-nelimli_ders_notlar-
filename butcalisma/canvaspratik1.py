"""🛠️ Temel Komutlar (Alet Çantası)
Canvas oluşturmak için: self.tuval = tk.Canvas(pencere, width=400, height=300, bg="white")

Çizim yapmak için şu 4 komut her şeye yeter:

Çizgi: create_line(x1, y1, x2, y2, fill="renk", width=kalınlık)

Kutu: create_rectangle(x1, y1, x2, y2, fill="dolgu_rengi", outline="çerçeve_rengi")

Daire/Elips: create_oval(x1, y1, x2, y2) (Mantığı kutu gibidir, o kutunun içine sığan daireyi çizer).

Yazı: create_text(x, y, text="Merhaba", fill="renk")"""

import tkinter as tk


class ResimDersi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Canvas 101")

        # 1. Tuvali Oluştur (400x300 boyutunda)
        self.tuval = tk.Canvas(self.pencere, width=400, height=300, bg="skyblue")
        self.tuval.pack()

        # 2. Güneş Çiz (Sol Üst)
        # x1=20, y1=20 (Sol üst köşe) -> x2=80, y2=80 (Sağ alt köşe)
        self.tuval.create_oval(20, 20, 80, 80, fill="yellow", outline="orange", width=5)

        # 3. Çimenlik Çiz (En Alt)
        # x1=0, y1=280 (Soldan başla, aşağıda) -> x2=400, y2=280 (Sağa kadar git)
        self.tuval.create_line(0, 280, 400, 280, fill="green", width=50)

        # 4. Evin Gövdesi (Kutu)
        # Ortada bir yer
        self.tuval.create_rectangle(
            150, 150, 250, 280, fill="gray", outline="black", width=5
        )

        # 5. Evin Çatısı (Çizgi ile Üçgen olmaz, Poligon gerekir ama çizgiyle yapalım)
        # Çatı mantığı: Sol alt -> Tepe -> Sağ alt
        self.tuval.create_line(150, 150, 200, 100, fill="red", width=5)  # Sol kenar
        self.tuval.create_line(200, 100, 250, 150, fill="red", width=5)  # Sağ kenar

        # İmza Atalım
        self.tuval.create_text(350, 290, text="Ressam: Ben", fill="black")

        self.pencere.mainloop()


ResimDersi()
