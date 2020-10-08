import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import  tabulate
import json



istek = requests.get("http://www.altinkaynak.com/Doviz/Kur/Guncel")
corba = BeautifulSoup(istek.content,'lxml')
tablo = corba.find('table', class_='table')



pandaVeri = pd.read_html(str(tablo))[0].rename(
    columns={
        'Unnamed: 0'    : 'Birim',
        'Unnamed: 1'    : 'sil',
        'Unnamed: 5'    : 'sil',
        '₺ ₺'         : 'sil',
    }
).drop(columns='sil').dropna()

# print(pandaVeri)

jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
# print(jsonVeri)


jsonCikti = json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
#print(jsonCikti)

gorselVeri = tabulate(pandaVeri, headers='keys', tablefmt='fancy_grid')
print(gorselVeri)

# anahtarlar = [anahtar for anahtar in jsonVeri[0].keys()]
# print(anahtarlar)

for anahtar in jsonVeri[0].keys():
    anahtarlar = anahtar













