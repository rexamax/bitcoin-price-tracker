import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate']
    return price

if __name__ == "__main__":
    price = get_bitcoin_price()
    print(f"Current Bitcoin price: ${price}")
