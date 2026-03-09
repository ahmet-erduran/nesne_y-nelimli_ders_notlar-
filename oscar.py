from tkinter import *

class Sinav:
    def __init__(self):
        pencerem = Tk()
        # ... Arayüz Kodları (Label, Grid vs.) ...
        
        # 1. DOSYAYI OKU VE TÜRLERİ AL (Tek Satırda Küme)
        dosya = open("Oscars.txt", "r")
        # Süslü parantez {} KÜME demektir (Tekrarları siler)
        self.filmturu = {satir.split(',')[1].strip() for satir in dosya} 
        dosya.close() # Dosyayı kapatmayı unutma
        
        # 2. SIRALA VE LİSTEYE ÇEVİR
        self.L = sorted(list(self.filmturu))
        
        # 3. SOL KUTUYA YÜKLE
        self.tursecim = StringVar()
        self.turlistesi = Listbox(pencerem, listvariable=self.tursecim)
        self.turlistesi.bind("<<ListboxSelect>>", self.filmgetir)
        self.turlistesi.grid(row=1, column=0)
        
        self.tursecim.set(tuple(self.L)) # Tuple yapıp basıyoruz
        
        # ... Sağ Kutu Kodları ...
        self.gelenfilmler = StringVar() # Sağ kutu için değişken
        self.filmlistesi = Listbox(pencerem, listvariable=self.gelenfilmler)
        self.filmlistesi.grid(row=1, column=1)

        pencerem.mainloop()

    def filmgetir(self, event):
        # Seçileni Al
        degerim = self.turlistesi.get(self.turlistesi.curselection())
        
        # 4. TEKRAR DOSYA OKU VE FİLTRELE (Tek Satırda Liste)
        # Köşeli parantez [] LİSTE demektir
        filmler = [
            satir.split(',')[0]                  # Filmin adını al
            for satir in open("Oscars.txt", "r") # Dosyayı satır satır gez
            if satir.split(',')[1].strip() == degerim # Eğer türü eşleşiyorsa
        ]
        
        # 5. SAĞ KUTUYA YÜKLE
        self.gelenfilmler.set(tuple(filmler))

Sinav()