import tkinter

def main():
    pencere=tkinter.Tk()
    pencere.title("liste")

    liste=tkinter.Listbox(pencere)
    liste.grid(row=0,column=0)
    dosya=open("sehirler.txt","r")

    for satir in dosya:
        satir.rstrip("\n")
        liste.insert(tkinter.END,satir)

    dosya.close()
    pencere.mainloop()
if __name__ =="__main__":
    main()


