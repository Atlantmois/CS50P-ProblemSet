import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    bitcoin_num = float(sys.argv[1])
    api_key = "Your-Api-Key"   #replace it with your API
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
    response = requests.get(url)
    price_usd = float(response.json()["data"]["priceUsd"])
    amount = price_usd * bitcoin_num
    print(f"${amount:,.4f}")
except requests.exceptions.RequestException:
    sys.exit("Api Error")
except ValueError:
    sys.exit("Command-line argument is not a number")    
