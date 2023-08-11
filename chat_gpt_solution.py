import requests
from config import API_TOKEN, SECRET_KEY
# Замените на свой API-ключ и секретный ключ
API_KEY = API_TOKEN
SECRET_KEY = SECRET_KEY
import requests
import time

# Установите URL Binance API
BASE_URL = 'https://api.binance.com/api/v3'

# Символ пары для BTC/USDT
symbol = 'BTCUSDT'


def get_hourly_price_change():
    # Получение свечей за последний час, интервал 1 час
    interval = '1h'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': 1  # Количество свечей
    }

    # Выполнение запроса
    response = requests.get(f'{BASE_URL}/klines', params=params)

    if response.status_code == 200:
        kline = response.json()[0]
        price_change = (float(kline[4]) - float(kline[1])) / float(kline[1]) * 100
        return price_change
    else:
        return None


# Бесконечный цикл для автоматического обновления каждый час
while True:
    price_change = get_hourly_price_change()
    if price_change is not None:
        print(f'Изменение цены BTC за последний час: {price_change:.2f}%')
    else:
        print('Ошибка при выполнении запроса')

    # Подождать 1 час перед следующим запросом
    time.sleep(3600)  # 3600 секунд = 1 час