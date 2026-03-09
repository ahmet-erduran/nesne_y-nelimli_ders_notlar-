import tkinter as tk


class OkulSistemi:
    def __init__(self):

        self.pencere = tk.Tk()
        self.pencere.title("Öğrenci Arama")

        # Arama Kutusu
        tk.Label(self.pencere, text="Bölüm Adı:").pack()
        self.arama_var = tk.StringVar()  # StringVar kullandım
        self.entry = tk.Entry(self.pencere, textvariable=self.arama_var)
        self.entry.pack()

        # Buton
        btn = tk.Button(self.pencere, text="Getir", command=self.ara)
        btn.pack(pady=5)

        # Sonuç Listesi
        self.sonuc_listesi = tk.Listbox(self.pencere)
        self.sonuc_listesi.pack()

        self.pencere.mainloop()

    def ara(self):
        aranan_bolum = self.arama_var.get()  # StringVar'dan oku
        self.sonuc_listesi.delete(0, tk.END)  # Listeyi temizle

        try:
            with open("okul.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    # Satır: "Bilgisayar,Ali\n" -> Parçala -> ["Bilgisayar", "Ali"]
                    parcalar = satir.strip().split(",")
                    bolum = parcalar[0]
                    isim = parcalar[1]

                    # Eğer aranan bölümle, satırdaki bölüm aynıysa
                    if bolum == aranan_bolum:
                        self.sonuc_listesi.insert(tk.END, isim)
        except FileNotFoundError:
            print("Dosya yok!")


if __name__ == "__main__":
    OkulSistemi()
