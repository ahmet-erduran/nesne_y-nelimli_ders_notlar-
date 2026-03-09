import tkinter as tk
import pickle

def main():
    pencere = tk.Tk()
    pencere.title("Rehber")
    pencere.geometry("500x400")

    def kaydet():
        #verileri al pickle yap
        gelen_isim=isim_kutusu.get()
        gelen_tel=telefon.get()

        kisi={"ad" : gelen_isim,"telefon":gelen_tel}

        dosya=open("rehber.dat","ab")
        pickle.dump(kisi,dosya)
        dosya.close()
        #kutuları temizle
        isim_kutusu.delete(0,tk.END)
        telefon.delete(0,tk.END)
        print("Kayıt Başarılı")
     
    def listele():
        rehberListesi.delete(0,tk.END)     
        dosya=open("rehber.dat","rb")

        while True:
            try:
                    #kişiyi oku
                    okunan_kisi = pickle.load(dosya)
                    #ekrana yazılacak metni hazırla
                    yazi = (f"{okunan_kisi['ad']} - {okunan_kisi['telefon']}")
                    #listboxa ekle
                    rehberListesi.insert(tk.END,yazi)
            except EOFError:
                    break
        dosya.close()


#adsoyad , numara ve liste
    tk.Label(pencere,text="İsim: ",bg="white").grid(row=0,column=0)
    isim_kutusu=tk.Entry(pencere)
    isim_kutusu.grid(row=0,column=1)

    tk.Label(pencere,text="Telefon: ",bg="white").grid(row=1,column=0)
    telefon=tk.Entry(pencere)
    telefon.grid(row=1,column=1)

    tk.Label(pencere,text="Telefon Rehberi: ",bg="white").grid(row=2,column=0)
    rehberListesi=tk.Listbox(pencere)
    rehberListesi.grid(row=2,column=1)
#menu
    ana_serit=tk.Menu(pencere)
    pencere.config(menu=ana_serit)
    dosya_menu=tk.Menu(ana_serit)
    dosya_menu.add_command(label="Kaydet",command=kaydet)
    dosya_menu.add_command(label="Listele",command=listele)
    ana_serit.add_cascade(label="Dosya",menu=dosya_menu)

    pencere.mainloop()

if __name__ == "__main__":
    main()