import tkinter as tk


class YillarUygulamasi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Yıl Uygulaması")
        self.pencere.geometry("300x200")

        # 1. ADIM: Önce Scrollbar'ı oluştur (Henüz bir şeye bağlı değil)
        # tk.RIGHT ve tk.Y kullandık.
        cubuk = tk.Scrollbar(self.pencere)
        cubuk.pack(side=tk.RIGHT, fill=tk.Y)

        # 2. ADIM: Listbox'ı oluştur ve 'yscrollcommand' ile çubuğa bağla
        # Artık 'cubuk' var olduğu için hata vermez.
        self.yillist = tk.Listbox(self.pencere, yscrollcommand=cubuk.set)
        self.yillist.pack(side=tk.LEFT)

        # 3. ADIM: Çubuğa "Listeyi kontrol et" emrini ver (Çift yönlü bağ tamamlandı)
        cubuk.config(command=self.yillist.yview)

        for x in range(1900, 2026):
            self.yillist.insert(tk.END, x)

        self.pencere.mainloop()


# Çalıştır
YillarUygulamasi()
