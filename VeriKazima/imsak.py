import requests
from datetime import datetime

def ezanVakti(il):
    istek = f"https://www.sabah.com.tr/json/getpraytimes/{il}"
    json_veri = requests.get(istek).json()["List"][0]

    imsak = datetime.fromtimestamp(int(json_veri["Imsak"].split("(")[1][:-5]))
    gunes = datetime.fromtimestamp(int(json_veri["Gunes"].split("(")[1][:-5]))
    ogle = datetime.fromtimestamp(int(json_veri["Ogle"].split("(")[1][:-5]))
    ikindi = datetime.fromtimestamp(int(json_veri["Ikindi"].split("(")[1][:-5]))
    aksam = datetime.fromtimestamp(int(json_veri["Aksam"].split("(")[1][:-5]))
    yatsi = datetime.fromtimestamp(int(json_veri["Yatsi"].split("(")[1][:-5]))

    mesaj = f"İmsak    : {str(imsak).split()[1]}\n"
    mesaj += f"Güneş    : {str(gunes).split()[1]}\n"
    mesaj += f"Öğle     : {str(ogle).split()[1]}\n"
    mesaj += f"İkindi   : {str(ikindi).split()[1]}\n"
    mesaj += f"Akşam    : {str(aksam).split()[1]}\n"
    mesaj += f"Yatsı    : {str(yatsi).split()[1]}\n"


    return mesaj

print("Malatya ;")
print(ezanVakti("malatya"))

print("Istanbul ;")
print(ezanVakti("istanbul"))




















