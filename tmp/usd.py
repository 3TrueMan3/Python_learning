import requests
import json


def get_currency_exchange():
    url = "https://api.tinkoff.ru/v1/currency_rates"
    r = requests.get(url).json()
    rate_dict = (r["payload"]["rates"])  # получаем массив rates, который содержит всё что нам надо

    for rate in rate_dict:
        if rate["category"] == "DebitCardsOperations":
            from_curr = rate['fromCurrency']
            to_curr = rate['toCurrency']
            print(from_curr.get('name'), "to", to_curr.get('name'))
            print("sell: ", rate["sell"], "\n", "buy: ", rate["buy"])


get_currency_exchange()
