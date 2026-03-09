def main():
  
    dosya= open("birinciSoruDosya.txt","a",encoding="utf-8")
    for i in range(5):
        ders = str(input("dersin adını giriniz: "))
        dersnotu = str(input("dersin notunu giriniz: "))

        dosya.write(ders + ":" + dersnotu + "\n")

    dosya.close()


    okunan_dosya=open("dosya.txt","r",encoding="utf-8")
    for satir in okunan_dosya:
        print(satir.rstrip("\n"))

    okunan_dosya.close()

if __name__ == "__main__":
    main()


