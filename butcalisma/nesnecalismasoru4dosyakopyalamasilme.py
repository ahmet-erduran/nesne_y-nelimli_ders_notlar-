import os

def main():
    okunan_dosya = open("stok.txt", "r", encoding="utf-8")
    gecici_dosya = open("gecici.txt", "w", encoding="utf-8")   
    silinecek = input("Silmek istediğinizi yazınız: ")
    
    for satir in okunan_dosya:
        parcalar = satir.split(',')
        
        urun_adi = parcalar[0] 

        if urun_adi.strip() != silinecek:
            gecici_dosya.write(satir)

    okunan_dosya.close()
    gecici_dosya.close()

    os.remove("stok.txt")
    os.rename("gecici.txt", "stok.txt")
    
    print("İşlem tamamlandı.")

if __name__ == "__main__":
    main()