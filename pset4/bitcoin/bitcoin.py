import requests
import sys
import json

args = list(sys.argv)

try:
    bitcoin = float(args[1])
except:
    sys.exit('Error')

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r_dict = json.loads(r.text)
    bit_price = r_dict['bpi']['USD']['rate_float']
except requests.RequestException:
    pass

print(f"${bitcoin*bit_price:,.4f}")