import tkinter as tk

def sepete_ekle():
    # 1. Soldaki listeden seçilenin indeksini al
    secilen = liste_urunler.curselection()
    indeks = secilen[0]
    # 2. Veriyi al
    urun = liste_urunler.get(indeks)
        
    # 3. Sağdaki listeye ekle
    liste_sepet.insert(tk.END, urun)
        
    # 4. (Opsiyonel) Soldakinden silmek istersen:
    #liste_urunler.delete(indeks)

pencere = tk.Tk()
pencere.title("Örnek 3 - Sepet")
pencere.geometry("300x200")

# Sol Liste (Ürünler)
lbl1 = tk.Label(pencere, text="Ürünler")
lbl1.grid(row=0, column=0)

liste_urunler = tk.Listbox(pencere)
liste_urunler.grid(row=1, column=0)
# Örnek veri ekleyelim
for u in ["Bilgisayar", "Mouse", "Klavye", "Kulaklık"]:
    liste_urunler.insert(tk.END, u)

# Buton (Ortada)
btn = tk.Button(pencere, text="Sepete Ekle >>", command=sepete_ekle)
btn.grid(row=1, column=1, padx=10)

# Sağ Liste (Sepet)
lbl2 = tk.Label(pencere, text="Sepetim")
lbl2.grid(row=0, column=2)

liste_sepet = tk.Listbox(pencere)
liste_sepet.grid(row=1, column=2)

pencere.mainloop()