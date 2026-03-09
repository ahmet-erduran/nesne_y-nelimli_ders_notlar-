import pickle

def main():
    marka=str(input("Araba Markası Giriniz: "))
    model=str(input("Araba Modeli Giriniz: "))
    fiyat=str(input("Araba Fiyatı Giriniz: "))

    arac_dict={'aracin_markasi':marka,'aracin_modeli':model,'aracin_fiyati':fiyat}
    
    dosya=open("araclar.dat","ab")
    pickle.dump(arac_dict,dosya)
    dosya.close()

if __name__ == "__main__":
    main()