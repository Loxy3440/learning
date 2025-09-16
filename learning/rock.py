import tkinter as tk
from tkinter import messagebox
import random

şifre = "yfya1234"

input = input("Şifreyi giriniz: ")
if input != şifre:
    print("Şifre yanlış! Program kapatılıyor.")
    exit()



# Pencere oluştur
pencere = tk.Tk()
pencere.title("Taş-Kağıt-Makas")
pencere.geometry("350x200")

# Değişkenler
kullanici_skor = 0
bilgisayar_skor = 0

# Skor etiketleri
skor_label = tk.Label(pencere, text="Skor: 0 - 0", font=("Arial", 14))
skor_label.pack(pady=10)

sonuc_label = tk.Label(pencere, text="Seçim yap!", font=("Arial", 12))
sonuc_label.pack(pady=5)

# Seçim butonları
def oyna(secim):
    global kullanici_skor, bilgisayar_skor
    
    secimler = ["taş", "kağıt", "makas"]
    bilgisayar_secimi = random.choice(secimler)
    
    # Kazanma durumları
    if secim == bilgisayar_secimi:
        sonuc = "Berabere!"
    elif (secim == "taş" and bilgisayar_secimi == "makas") or \
         (secim == "kağıt" and bilgisayar_secimi == "taş") or \
         (secim == "makas" and bilgisayar_secimi == "kağıt"):
        sonuc = "Kazandın! 🎉"
        kullanici_skor += 1
    else:
        sonuc = "Kaybettin! 😢"
        bilgisayar_skor += 1
    
    # Sonuçları güncelle
    sonuc_label.config(text=f"Bilgisayar: {bilgisayar_secimi}\n{sonuc}")
    skor_label.config(text=f"Skor: {kullanici_skor} - {bilgisayar_skor}")

# Butonları oluştur
buton_frame = tk.Frame(pencere)
buton_frame.pack(pady=10)

tk.Button(buton_frame, text="Taş", command=lambda: oyna("taş"), width=8).pack(side=tk.LEFT, padx=5)
tk.Button(buton_frame, text="Kağıt", command=lambda: oyna("kağıt"), width=8).pack(side=tk.LEFT, padx=5)
tk.Button(buton_frame, text="Makas", command=lambda: oyna("makas"), width=8).pack(side=tk.LEFT, padx=5)

# Pencereyi başlat
pencere.mainloop()