import tkinter as tk


class HesapMakinesi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Hesap Makinesi")
        self.pencere.geometry("400x300")

        self.sayi1 = tk.IntVar()
        self.sayi1ent = tk.Entry(self.pencere, textvariable=self.sayi1)
        self.sayi1ent.grid(row=0, column=0, padx=15)

        self.sayi2 = tk.IntVar()
        self.sayi2ent = tk.Entry(self.pencere, textvariable=self.sayi2)
        self.sayi2ent.grid(row=0, column=2, pady=40, padx=40)

        self.hesaplayici = tk.Button(self.pencere, text="Hesapla", command=self.topla)
        self.hesaplayici.grid(row=1, column=1)

        self.sonuc = tk.Label(self.pencere, text="x", fg="green", font="Arial 20")
        self.sonuc.grid(row=3, column=1)

        self.pencere.mainloop()

    def topla(self):
        self.sonucmetin = self.sayi1.get() + self.sayi2.get()

        self.sonuc.config(text=self.sonucmetin)


HesapMakinesi()
