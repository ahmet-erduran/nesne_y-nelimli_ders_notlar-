import pickle
def main():
        cikis_dosyasi = open("veriler.dat","ab")

        devam="e"

        print("-- Öğrenci kayıt sistemi --")

        while devam.lower()=="e":
            ad=input("isim: ")
            no=input("ögrenci no: ")
            ort=input("not ortalamasi: ")

            ogrenci_karti = {
                "isim" : ad,
                "numara" : no,
                "ortalama" : ort
            }

            pickle.dump(ogrenci_karti,cikis_dosyasi)
            print("kayıt eklendi")

            devam = input("başka veri e/h")

        cikis_dosyasi.close()
        
        print("dosyadaki bütün kayıtlar")

        giris_dosyasi= open("veriler.dat","rb")

        dosya_sonu= False

        while not dosya_sonu:
            try:
                    okunan_ogrenci=pickle.load(giris_dosyasi)

                    print(f"İsim: {okunan_ogrenci['isim']}")
                    print(f"No  : {okunan_ogrenci['numara']}")
                    print(f"Not : {okunan_ogrenci['ortalama']}")
                    print("-" * 15)
            except EOFError:
                  dosya_sonu = True

        giris_dosyasi.close()
if __name__ == "__main__":
      main()