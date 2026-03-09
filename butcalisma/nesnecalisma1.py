import os  # Dosya işlemleri için kütüphaneyi çağırdık

def main():
    try:
        devam = 'e'
        # encoding='utf-8' ekledik ki Türkçe karakter sorunu olmasın
        dosya = open('calisanlar.txt', 'a', encoding='utf-8')

        while devam.lower() == 'e':
            print('---Çalışan Verilerini Giriniz---')
            isim = input("İsim: ")
            sicil = input("Sicil No: ")
            bolum = input("Bölüm: ")

            # Her bilgiyi yazıp alt satıra geçiyoruz
            dosya.write(isim + "\n")
            dosya.write(sicil + "\n")
            dosya.write(bolum + "\n")

            devam = input("devam etmek istiyor musunuz E/H : ")

        dosya.close()
        print("Veriler calisanlar.txt dosyasına eklendi")

        # --- SİLME İŞLEMİ ---
        sil_secim = input("dosyadan çalışan silinecek mi ? E/H: ")

        if sil_secim.lower() == "e":
            aranan_isim = input("silinecek isim : ")
            bulundu = False

            # Okurken ve yazarken utf-8 kullanıyoruz
            eski_dosya = open("calisanlar.txt", "r", encoding='utf-8')
            gecici_dosya = open("temp.txt", "w", encoding='utf-8')

            # İlk satırı (ismi) okuyoruz
            isim = eski_dosya.readline()

            # DÜZELTME BURADA: " " (boşluk) yerine "" (hiçlik) kontrolü yapıyoruz
            # Veya kısaca "while isim:" diyebiliriz, dosya bitince döngü durur.
            while isim != "": 
                sicil = eski_dosya.readline()
                bolum = eski_dosya.readline()

                # Satır sonundaki \n karakterlerini temizle
                isim = isim.rstrip('\n')
                sicil = sicil.rstrip('\n')
                bolum = bolum.rstrip('\n')

                # Eğer okunan isim, silinecek isim DEĞİLSE geçici dosyaya yaz
                if isim != aranan_isim:
                    gecici_dosya.write(isim + '\n')
                    gecici_dosya.write(sicil + '\n')
                    gecici_dosya.write(bolum + '\n')
                else:
                    bulundu = True # Silinecek ismi bulduk, dosyaya yazmıyoruz (sildik)

                # Döngünün dönmesi için bir sonraki ismi oku
                isim = eski_dosya.readline()

            eski_dosya.close()
            gecici_dosya.close()

            # Dosya değiştirme işlemi
            os.remove("calisanlar.txt")
            os.rename("temp.txt", "calisanlar.txt")

            if bulundu:
                print(f"{aranan_isim} başarıyla silindi")
            else:
                print("Dosyada bulunamadı")
                
    except IOError:
        print("Dosya işlemi sırasında bir hata oluştu")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

if __name__ == "__main__":
    main()