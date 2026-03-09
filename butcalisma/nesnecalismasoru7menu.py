import tkinter

def main():
    pencere = tkinter.Tk()
    pencere.title("Menü ve Entry İlişkisi")
    pencere.geometry("300x200")

    tkinter.Label(pencere, text="Bir not giriniz:").pack(pady=10)

    not_kutusu = tkinter.Entry(pencere)
    not_kutusu.pack()

    def kutuyu_temizle():
        not_kutusu.delete(0, tkinter.END)
        print("Kutu temizlendi!")

    def konsola_yaz():
        veri = not_kutusu.get()
        print(f"Yazılan Not: {veri}")

    ana_serit = tkinter.Menu(pencere)
    pencere.config(menu=ana_serit)

    dosya_menu = tkinter.Menu(ana_serit, tearoff=0)

    dosya_menu.add_command(label="Konsola Yazdır", command=konsola_yaz)
    dosya_menu.add_command(label="Temizle", command=kutuyu_temizle) 
    dosya_menu.add_separator() 
    dosya_menu.add_command(label="Çıkış", command=pencere.destroy)

    ana_serit.add_cascade(label="Dosya", menu=dosya_menu)

    pencere.mainloop()

if __name__ == "__main__":
    main()