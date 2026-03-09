import tkinter as tk

class MerhabaUygulamasi:
    def __init__(self):
        # 1. Pencereyi "self.pencere" olarak oluşturuyoruz ki her yerden erişelim.
        self.pencere = tk.Tk()
        self.pencere.title("Soru 1 - Class Yapısı")
        self.pencere.geometry("300x200")

        # 2. Etiketi de "self" ile tanımla (Çünkü yazısını değiştireceğiz)
        self.etiket = tk.Label(self.pencere, text="Merhaba", font=("Arial", 14))
        self.etiket.pack(pady=20)

        # 3. Butona "self.tikla" fonksiyonunu bağla
        btn = tk.Button(self.pencere, text="Tıkla", command=self.tikla)
        btn.pack()

        self.pencere.mainloop()

    # Class'ın içindeki fonksiyonlara "self" parametresi zorunludur!
    def tikla(self):
        # self.etiket diyerek yukarıdaki etikete ulaşıyoruz
        self.etiket.config(text="Butona Basıldı!", fg="red")

# Çalıştırma Kodu
if __name__ == "__main__":
    MerhabaUygulamasi()