import tkinter as tk

class AynaUygulamasi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Soru 2 - StringVar")

        # 1. Özel Değişken Tanımlama
        self.veri = tk.StringVar() 
        self.veri.set("Buraya yazın...") # Başlangıç değeri

        # 2. Entry'ye Bağlama (textvariable)
        # Artık kutuya ne yazılırsa "self.veri" içinde tutulur.
        self.giris = tk.Entry(self.pencere, textvariable=self.veri)
        self.giris.pack(pady=10)

        btn = tk.Button(self.pencere, text="Aktar", command=self.aktar)
        btn.pack()

        self.sonuc_etiketi = tk.Label(self.pencere, text="...")
        self.sonuc_etiketi.pack(pady=10)

        self.pencere.mainloop()

    def aktar(self):
        # Kutunun içindekini değişken üzerinden alıyoruz (.get)
        yazi = self.giris.get()
        self.sonuc_etiketi.config(text=yazi)
        
        # İşlem bitince kutuyu kodla değiştirebiliriz (.set)
        #self.veri.set("Temizlendi") 

if __name__ == "__main__":
    AynaUygulamasi()