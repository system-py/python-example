import requests
import pandas as pd
import json
from tabulate import tabulate
from bs4 import BeautifulSoup

istek = requests.get("https://finans.haberler.com/")
corba = BeautifulSoup(istek.content,"lxml")
tablo = corba.find(class_="hbTableContent piyasa")

#print(tablo)

pandaVeri = pd.read_html(str(tablo))[0].rename(
    columns={
        "Yön": "sil"
    }
).drop(columns="sil").dropna()

print(pandaVeri)

jsonVeri = json.loads(pandaVeri.to_json(orient="records"))

#print(jsonVeri)

jsonCikti = json.dumps(jsonVeri,indent=2, sort_keys=False ,ensure_ascii=False)

# print(jsonCikti)


gorselVeri = tabulate(pandaVeri, headers="keys", tablefmt="fancy_grid")
# print(gorselVeri)

anahtarlar = [anahtar for anahtar in jsonVeri[0].keys()]

# print(anahtarlar)



