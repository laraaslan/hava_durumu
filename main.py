import requests
from tkinter import *


def hava_durumu(api_key, sehir):
    api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={sehir}"
    response = requests.get(api_url)

    if response.status_code == 200:
        hava_durumu_verisi = response.json()
        if "current" in hava_durumu_verisi:
            durum = hava_durumu_verisi["current"]["condition"]["text"]
            sicaklik = hava_durumu_verisi["current"]["temp_c"]
            nem = hava_durumu_verisi["current"]["humidity"]
            ruzgar_hizi = hava_durumu_verisi["current"]["wind_kph"]

            # Hava durumu bilgilerini güncelleme
            label_durum.config(text=f"Durum: {durum}")
            label_sicaklik.config(text=f"Sıcaklık: {sicaklik}°C")
            label_nem.config(text=f"Nem: {nem}%")
            label_ruzgar.config(text=f"Rüzgar Hızı: {ruzgar_hizi} km/s")
        else:
            print("Hava durumu verileri alınamadı.")
    else:
        print("Hava durumu verileri alınamadı.")


# API anahtarınız
api_key = "4bc3f1ea774a40399f1113347242703"

# Ana pencere
window = Tk()
window.title("Hava Durumu")
window.geometry("300x250")

# Şehir giriş alanı
label_sehir = Label(window, text="Şehir:")
label_sehir.pack()

entry_sehir = Entry(window)
entry_sehir.pack()

# Etiketler
label_durum = Label(window, text="Durum: ")
label_durum.pack()

label_sicaklik = Label(window, text="Sıcaklık: ")
label_sicaklik.pack()

label_nem = Label(window, text="Nem: ")
label_nem.pack()

label_ruzgar = Label(window, text="Rüzgar Hızı: ")
label_ruzgar.pack()


# Düğme işlevi
def action():
    sehir = entry_sehir.get()
    hava_durumu(api_key, sehir)


# Düğme
button = Button(window, text="Bilgileri Getir", command=action)
button.pack()

window.mainloop()
