import tkinter as tk


class GirisSistemi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Giriş Uygulaması")
        self.pencere.geometry("250x250")

        tk.Label(self.pencere, text="Kullanıcı Adı: ").grid(row=0, column=0)
        tk.Label(self.pencere, text="Şifre: ").grid(row=1, column=0)

        self.kullanici = tk.Entry(self.pencere)
        self.kullanici.grid(row=0, column=1)

        self.sifre = tk.Entry(self.pencere, show="*")
        self.sifre.grid(row=1, column=1, pady=10)

        tk.Button(
            self.pencere, text="Giriş Yap", font="Arial 12", command=self.GirisYap
        ).grid(row=2, column=1, pady=15)
        self.sonuclbl = tk.Label(self.pencere, text="", fg="red")
        self.sonuclbl.grid(row=3, column=1)

        self.pencere.mainloop()

    def GirisYap(self):

        indexkul = self.kullanici.get()
        indexsif = self.sifre.get()
        bulundu_mu = False

        dosyam = open("kullanicilar.txt", "r")
        for satir in dosyam:
            islenmis_satir = satir.strip().split(",")

            if islenmis_satir[0] == indexkul and islenmis_satir[1] == indexsif:
                bulundu_mu = True
                break
        if bulundu_mu == True:
            self.sonuclbl.config(text="Giriş Başarılı", fg="green")
        else:
            self.sonuclbl.config(text="Tekrar Deneyiniz")


GirisSistemi()
