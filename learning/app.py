şifre = "yfya1234"
sor = input("Şifreyi giriniz: ")
if sor != şifre:
    print("Şifre yanlış! Program kapatılıyor.")
    exit()

kullanıcı_adi = input("Adınız Nedir? ")
if kullanıcı_adi == "n":
    print("merhaba ne") 
else:
    print("sen kimsin , " + kullanıcı_adi)

yaş = int(input("yaşını söyle "))
if yaş == 15:
    print("Yaşıtsız ha ")
elif yaş < 15:
    print("Veletsin ha  ")
elif yaş > 15:
    print("Büyüksün ha  ")