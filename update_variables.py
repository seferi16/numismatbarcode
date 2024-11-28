import requests
from bs4 import BeautifulSoup
import os
import json

def round_price(price, decimal=2):
        if type(price) == str:
                return round(float(price.replace(".", "").replace(",", ".")), decimal)
        else:
                return round(price, decimal)


url = 'https://borsa.doviz.com/hisseler/altins1-darphane-altin-sertifikasi'  # Replace with the correct URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

s1_altin_span = soup.find('div', {
    'class': 'text-xl font-semibold text-white',
    'data-socket-key': 'ALTINS1',
    # 'data-socket-attr': 'S'
})
s1_altin_value = round_price(s1_altin_span.text.strip())

# Extract the value for "gram-altin"
gram_altin_span = soup.find('span', {'data-socket-key': 'gram-altin'})
gram_altin_value = round_price(gram_altin_span.text.strip()) if gram_altin_span else "Not found"

# Extract the value for "USD"
usd_span = soup.find('span', {'data-socket-key': 'USD'})
usd_value = round_price(usd_span.text.strip()) if usd_span else "Not found"

# Extract the value for "gumus"
gumus_span = soup.find('span', {'data-socket-key': 'gumus'})
gumus_value = round_price(gumus_span.text.strip()) if gumus_span else "Not found"

gold_silver_rate = round_price(gram_altin_value / gumus_value)
s1_tryg_rate = round_price((s1_altin_value*100) / gram_altin_value, 5)

# json_file = ""

data = {
        "xautryg" : {"value": gram_altin_value},
        "xagtryg" : {"value": gumus_value},
        "usdtry" : {"value": usd_value}
}

with open("numismatnettools/variables.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
