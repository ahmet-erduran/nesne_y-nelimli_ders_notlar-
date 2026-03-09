import tkinter as tk


class SayacUygulamasi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("İlk örnek sayaç")
        self.pencere.geometry("300x200")

        self.sayi = 0

        self.etiket = tk.Label(self.pencere, text=self.sayi)
        self.etiket.grid(row=0, column=0, columnspan=2, pady=20)

        self.artirbtn = tk.Button(self.pencere, text="Arttır", command=self.SayiyiArtir)
        self.artirbtn.grid(row=1, column=0, padx=10)

        self.azaltbtn = tk.Button(self.pencere, text="Azalt", command=self.SayiyiAzalt)
        self.azaltbtn.grid(row=1, column=1, padx=10)

        self.pencere.mainloop()

    def SayiyiArtir(self):
        self.sayi += 1
        self.etiket.config(text=str(self.sayi))

    def SayiyiAzalt(self):
        if self.sayi > 0:
            self.sayi -= 1
            self.etiket.config(text=str(self.sayi))
        else:
            print("Önce sayıyı artırın")


# Uygulamayı Başlat
SayacUygulamasi()
