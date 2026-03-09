from tkinter import *

def dosya_oku_ve_listele():
    try:
        with open("dunya.txt","r")as dosya:
            satirlar=dosya.readlines()
        liste_kutusu.delete(0,END)

        for satir in satirlar:

            liste_kutusu.insert(END,satir.rstrip())

        durum_etiketi.config(text="Dosya başarıyla okundu")

    except FileNotFoundError:
        durum_etiketi.config(text="Dunya.txt bulunamadı")

pencere = Tk()
pencere.title("Ülke Listesi")

btn_oku = Button(pencere , text= "Dosyadan ülkeleri listele" , command=dosya_oku_ve_listele)
btn_oku.pack(pady=10)

liste_kutusu = Listbox(pencere,height=10,width=30)
liste_kutusu.pack(pady=10)

durum_etiketi = Label(pencere, text="Henüz veri çekilmedi.")
durum_etiketi.pack()

pencere.mainloop()