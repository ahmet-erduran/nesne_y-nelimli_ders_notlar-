import tkinter as tk

def doldur():
    liste.delete(0, tk.END)

    dosya=open("vitaminler.txt", "r", encoding="utf-8") 
    for satir in dosya:
                # Satır: "Elma,A vitamini" -> Parçala -> ["Elma", "A vitamini"]
                kelimeler = satir.split(',')
                liste.insert(tk.END, kelimeler[0])
    dosya.close()
# DÜZELTME 1: (event) parametresi ekledik!
def meyveVitaminler(event):
    vitaminler.delete(0, tk.END) 
    # DÜZELTME 2: 'vitaminler' değil 'liste'den seçim alıyoruz
    secilen_indeksler = liste.curselection()       
    secilen_indeks = secilen_indeksler[0]       
    # DÜZELTME 3: İndeksi (0) değil, metni ("Elma") alıyoruz
    secilen_meyve_adi = liste.get(secilen_indeks)

    # Şimdi dosyada ara
    dosyam=open("vitaminler.txt", "r", encoding="utf-8") 
    for satir in dosyam:
            kelimeler = satir.strip().split(",") 
                # Dosyadaki isim (kelimeler[0]) ile seçilen isim aynı mı?
            if kelimeler[0] == secilen_meyve_adi:
                    # Eşleşti! Vitamin bilgisini (kelimeler[1]) ekle
                vitaminler.insert(tk.END, kelimeler[1])
    dosyam.close()

pencere = tk.Tk()
pencere.title("Meyve Vitamin Programı")
pencere.geometry("300x400")

btn = tk.Button(pencere, text="Meyveleri Getir", command=doldur)
btn.pack()

tk.Label(pencere, text="Meyve Seçiniz:").pack()
liste = tk.Listbox(pencere)
liste.pack()
liste.bind("<<ListboxSelect>>", meyveVitaminler)

tk.Label(pencere, text="Vitamin Değeri:").pack()
vitaminler = tk.Listbox(pencere)
vitaminler.pack()

pencere.mainloop()