import tkinter as tk

class SecimUygulamasi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Dil Seçiniz")

        self.liste = tk.Listbox(self.pencere)
        self.liste.pack(pady=20)
        
        diller = ["Python", "C#", "Java", "C++", "JavaScript"]
        for dil in diller:
            self.liste.insert(tk.END, dil)

        # <<ListboxSelect>> olayını "secildi" fonksiyonuna bağla
        self.liste.bind("<<ListboxSelect>>", self.secildi)

        self.pencere.mainloop()

    # Event (olay) parametresi zorunludur!
    def secildi(self, event):
        # Seçilen satırın numarasını al
        indeksler = self.liste.curselection()      
        secilen_dil = self.liste.get(indeksler[0])           
            # Pencere başlığını değiştir
        self.pencere.title(f"Seçilen: {secilen_dil}")

if __name__ == "__main__":
    SecimUygulamasi()