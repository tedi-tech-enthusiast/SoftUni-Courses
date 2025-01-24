import requests


def convert_currencies(amount):
    api_key ='b1ecae393cc225fd672b9eb3'
    url= f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        conversion_rate = data['conversion_rates']['USD']
        dollars = amount * conversion_rate

        return f'{dollars:.3f}'
    else:
        return 'Error fetching exchange rate'

currant_value = int(input())
usd = convert_currencies(currant_value)



print(f'{currant_value} British pouds is equal to {usd} US dollars.')