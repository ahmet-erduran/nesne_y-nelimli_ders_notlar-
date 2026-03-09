import tkinter as tk

def secileni_goster(event):
    # 1. Seçilen satırın İNDEKS numarasını al (Örn: 0, 1, 2...)
    # curselection() bize bir demet verir (0,), içinden ilki lazım.
    secilen_indeksler = liste.curselection()
    indeks = secilen_indeksler[0]
    # 2. O indeksteki METNİ al (.get kullanıyoruz)
    veri = liste.get(indeks)
    # 3. Label'a yaz
    etiket.config(text=f"Seçilen: {veri}", fg="blue")
    lbl.config(text=veri)

pencere = tk.Tk()
pencere.title("Örnek 2")

liste = tk.Listbox(pencere)
liste.pack()
liste.insert(0, "Python")
liste.insert(1, "C#")
liste.insert(2, "Java")
liste.insert(3, "C++")

lbl=tk.Label(pencere,text="bir seçim yapınız")
lbl.pack()

# *** KRİTİK NOKTA ***
# Listeye "Tıklama" olayını bağlıyoruz. 
# Tıklanınca 'secileni_goster' fonksiyonu çalışacak.
liste.bind("<<ListboxSelect>>", secileni_goster)

etiket = tk.Label(pencere, text="Bir dil seçin...")
etiket.pack()

pencere.mainloop()