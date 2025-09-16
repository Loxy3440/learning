import random

şifre = "sifre"
sor = input("Şifreyi giriniz: ")
if sor != şifre:
    print("Şifre yanlış! Program kapatılıyor.")
    exit()



def sifre_oluştur(uzunluk=15):
    karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    sifre = "".join(random.choice(karakterler) for _ in range (uzunluk))
    return sifre
print("Oluşturulan Şifre: ", sifre_oluştur())
while True:
    devam = input("Başka bir şifre oluşturmak istiyor musunuz? (evet/hayır): ")
    if devam.lower() == "evet":
        print("Oluşturulan Şifre: ", sifre_oluştur())
    elif devam.lower() == "hayır":
        print("Şifre oluşturucu kapatılıyor.")
        break
    else:
        print("Lütfen 'evet' veya 'hayır' ile cevap verin.")