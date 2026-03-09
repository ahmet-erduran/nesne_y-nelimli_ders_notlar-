import tkinter as tk
import pickle


class SinemaArsivi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Sinema Rehberi")
        self.pencere.geometry("350x400")

        # --- VERİLERİ YÜKLE ---
        self.tum_filmler = []
        try:
            with open("filmler.pkl", "rb") as f:
                self.tum_filmler = pickle.load(f)
        except:
            print("Dosya bulunamadı!")

        # --- ARAYÜZ ---

        # 1. Arama Bölümü
        tk.Label(self.pencere, text="Film Ara (Ad veya Tür):").pack(pady=5)
        self.arama_kutusu = tk.Entry(self.pencere)
        self.arama_kutusu.pack()

        # Buton (command olduğu için 'event' YOK)
        btn_ara = tk.Button(self.pencere, text="Filtrele", command=self.ara)
        btn_ara.pack(pady=5)

        # 2. Liste Bölümü
        self.liste_kutusu = tk.Listbox(self.pencere)
        self.liste_kutusu.pack(pady=10)

        # Tıklama (bind olduğu için 'event' VAR)
        self.liste_kutusu.bind("<<ListboxSelect>>", self.detay_goster)

        # 3. Detay Bölümü
        self.etiket_detay = tk.Label(
            self.pencere, text="Detaylar...", fg="blue", font=("Arial", 11)
        )
        self.etiket_detay.pack(pady=20)

        # Başlangıçta tüm listeyi gösterelim
        self.listeyi_doldur(self.tum_filmler)

        self.pencere.mainloop()

    # --- FONKSİYONLAR ---

    def listeyi_doldur(self, gosterilecek_liste):
        # Listbox'ı temizle ve gelen listeyi ekle
        self.liste_kutusu.delete(0, tk.END)
        for film in gosterilecek_liste:
            self.liste_kutusu.insert(tk.END, film["ad"])

    def ara(self):  # Buton tetikliyor -> event YOK
        aranan = self.arama_kutusu.get().lower()  # Küçük harfe çevir

        # Geçici bir liste oluştur, eşleşenleri içine at
        filtrelenmis_liste = []
        for film in self.tum_filmler:
            # Adında VEYA Türünde geçiyorsa ekle
            if aranan in film["ad"].lower() or aranan in film["tur"].lower():
                filtrelenmis_liste.append(film)

        # Sadece bulunanları ekrana bas
        self.listeyi_doldur(filtrelenmis_liste)

    def detay_goster(self, event):  # Bind tetikliyor -> event VAR
        # 1. Tıklanan film ismini al
        secilen_indeks = self.liste_kutusu.curselection()

        if secilen_indeks:
            # Listbox'tan ismi çekiyoruz ("Matrix" gibi)
            secilen_isim = self.liste_kutusu.get(secilen_indeks)

            # 2. Bu ismi ANA LİSTEDE bulup detaylarını çek
            # (Filtreleme yaptığımız için indeksler karışabilir, isme göre aramak en garantisi)
            for film in self.tum_filmler:
                if film["ad"] == secilen_isim:
                    # Eşleşmeyi bulduk!
                    bilgi = f"Yönetmen: {film['yonetmen']}\nYıl: {film['yil']}\nTür: {film['tur']}"
                    self.etiket_detay.config(text=bilgi)
                    break  # Bulunca döngüden çık


SinemaArsivi()
