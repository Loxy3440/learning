şifre = "yfya1234"
sor = input("Şifreyi giriniz: ")
if sor != şifre:
    print("Şifre yanlış! Program kapatılıyor.")
    exit()



sayı1 = float(input("Birinci sayıyı girin: "))
işlem = input(" Hangi işlemi yapmak istiyorsunuz=(+,-,*,/): ")
sayı2 = float(input("İkinci sayıyı girin: "))
if işlem == "+":
    sonuc = sayı1 + sayı2   
elif işlem == "-":
    sonuc = sayı1 - sayı2   
elif işlem == "*":
    sonuc = sayı1 * sayı2   
elif işlem == "/":
    sonuc = sayı1 / sayı2
else:
    sonuc = "yapacagın isi sikim"

print(" Sonuç : ", sonuc)

while True:
    devam = input("Başka bir işlem yapmak istiyor musunuz? (evet/hayır): ")
    if devam.lower() == "evet":
        sayı1 = float(input("Birinci sayıyı girin: "))
        işlem = input(" Hangi işlemi yapmak istiyorsunuz=(+,-,*,/): ")
        sayı2 = float(input("İkinci sayıyı girin: "))
        if işlem == "+":
            sonuc = sayı1 + sayı2   
        elif işlem == "-":
            sonuc = sayı1 - sayı2   
        elif işlem == "*":
            sonuc = sayı1 * sayı2   
        elif işlem == "/":
            sonuc = sayı1 / sayı2
        else:
            sonuc = "yapacagın is is değil yeğen"
        print(" Sonuç : ", sonuc)
    elif devam.lower() == "hayır":
        print("Hesap makinesi kapatılıyor.")
        break
    else:
        print("Lütfen 'evet' veya 'hayır' ile cevap verin.")