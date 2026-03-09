import tkinter as tk


class ListeUygulamasi:
    def __init__(self):
        self.pencere = tk.Tk()

        # 1. Scrollbar Oluştur
        kaydirma_cubugu = tk.Scrollbar(self.pencere)
        kaydirma_cubugu.pack(side=tk.RIGHT, fill=tk.Y)  # Sağa yasla

        # 2. Listbox Oluştur
        self.liste = tk.Listbox(self.pencere, yscrollcommand=kaydirma_cubugu.set)
        self.liste.pack(side=tk.LEFT, fill=tk.BOTH)

        # 3. Çubuğa "Listeyi kontrol et" emri ver
        kaydirma_cubugu.config(command=self.liste.yview)

        # İçini dolduralım (1'den 100'e)
        for i in range(1, 101):
            self.liste.insert(tk.END, f"Satır {i}")

        self.pencere.mainloop()


if __name__ == "__main__":
    ListeUygulamasi()
