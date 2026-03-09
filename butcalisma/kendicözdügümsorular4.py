import tkinter as tk


class Arkaplan:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Background Changer")
        self.pencere.geometry("250x250")

        self.listem = tk.Listbox(self.pencere)
        self.listem.pack()

        for x in ["Red", "Blue", "Green", "Yellow"]:
            self.listem.insert(tk.END, x)

        self.listem.bind("<<ListboxSelect>>", self.renkdegistir)
        self.pencere.mainloop()

    def renkdegistir(self, event):
        secilen = self.listem.curselection()
        secilen_index = secilen[0]
        sec = self.listem.get(secilen_index)
        self.pencere.config(bg=sec)


Arkaplan()
