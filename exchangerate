# Установить библиотеку - pip install requests
import requests

def get_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def convert_currency(amount, from_currency, to_currency):
    rate = get_rate(from_currency, to_currency)
    return amount * rate

if __name__ == '__main__':
    # Убрано использование API ключа, т.к. он здесь уже не нужен
    from_currency = input("Введите исходную валюту (например, USD): ").upper()
    to_currency = input("Введите целевую валюту (например, EUR): ").upper()
    amount = float(input("Введите сумму для конвертации: "))

    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} равно {result:.2f} {to_currency}")
