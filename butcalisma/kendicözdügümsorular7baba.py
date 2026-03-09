import tkinter as tk
import pickle


class kitap:
    def __init__(self):

        self.pencerem = tk.Tk()
        self.pencerem.title("kitap")
        self.pencerem.geometry("250x250")

        tk.Label(self.pencerem, text="Kitap ara:").grid(row=0, column=0)
        self.aramaent = tk.Entry(self.pencerem)
        self.aramaent.grid(row=0, column=1)
        self.aramabtn = tk.Button(
            self.pencerem, text="Aramayı Başlat", relief="raised", command=self.ara
        )
        self.aramabtn.grid(row=1, column=0)

        self.liste = tk.Listbox(self.pencerem)
        self.liste.grid(row=1, column=1)
        self.liste.bind("<<ListboxSelect>>", self.detaylandir)

        self.detaylbl = tk.Label(self.pencerem, text="Kitap Detayları")
        self.detaylbl.grid(row=2, column=1)

        self.pencerem.mainloop()

    def detaylandir(self, event):
        secilen = self.liste.curselection()
        secilenkitap = self.liste.get(secilen[0])

        dosyam = open("kitaplar.dat", "rb")
        butundict = pickle.load(dosyam)

        for satir in butundict:
            if satir["ad"] == secilenkitap:
                yazar = satir["yazar"]
                sayfa = satir["sayfa"]
                self.detaylbl.config(text=f"Yazar: {yazar} | Sayfa: {sayfa}")

    def ara(self):
        aranankitap = self.aramaent.get()
        self.liste.delete(0, tk.END)

        dosyam = open("kitaplar.dat", "rb")
        butundict = pickle.load(dosyam)

        for satir in butundict:
            if aranankitap.lower() in satir["ad"].lower():
                self.liste.insert(tk.END, satir["ad"])

        dosyam.close()


kitap()
