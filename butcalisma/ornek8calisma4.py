import tkinter as tk

# Tüm veriyi hafızada tutmak için global bir sözlük
sehir_verileri = {}

def dosya_oku():
    f= open("sehirler.txt", "r", encoding="utf-8") 
    for satir in f:
            # Satır: "Ankara,06,IcAnadolu\n"
            parcalar = satir.strip().split(',') 
            # parcalar[0]=Ankara, parcalar[1]=06, parcalar[2]=Bolge             
            ad = parcalar[0]
                
            # Sözlüğe kaydedelim: "Ankara" -> ["06", "IcAnadolu"]
            sehir_verileri[ad] = [parcalar[1], parcalar[2]]
                
            # Listeye sadece adını ekle
            liste.insert(tk.END, ad)
    f.close()
    
def detay_goster(event):
    # 1. Hangi şehre tıklandı?
    indeks = liste.curselection()
    sehir_adi = liste.get(indeks[0])
        
    # 2. Sözlükten o şehrin bilgilerini çek
    bilgiler = sehir_verileri[sehir_adi] # ['06', 'IcAnadolu'] gelir
        
    # 3. Entry kutularını temizle ve doldur
    # Plaka
    ent_plaka.delete(0, tk.END)
    ent_plaka.insert(0, bilgiler[0])
        
    # Bölge
    ent_bolge.delete(0, tk.END)
    ent_bolge.insert(0, bilgiler[1])

pencere = tk.Tk()
pencere.title("Örnek 4 - Şehir Detay")

# Liste
liste = tk.Listbox(pencere)
liste.grid(row=0, column=0)
liste.bind("<<ListboxSelect>>", detay_goster)

# Detay Alanları
tk.Label(pencere, text="Plaka Kodu:").grid(row=0, column=1)
ent_plaka = tk.Entry(pencere)
ent_plaka.grid(row=0, column=2)

tk.Label(pencere, text="Bölgesi:").grid(row=1, column=1)
ent_bolge = tk.Entry(pencere)
ent_bolge.grid(row=1, column=2)

# Program başlarken verileri yükle
dosya_oku()

pencere.mainloop()