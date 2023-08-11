import pandas as pd
from binance import Client
import time
import datetime as dt
from get_testingmodel_data import r_squared
from config import API_TOKEN, SECRET_KEY


client = Client(API_TOKEN, SECRET_KEY)

def get_binanceklines(symbol = 'ETHUSDT', interval = Client.KLINE_INTERVAL_1MINUTE, limit = 60,):
    binance=client
    klines = binance.get_klines(symbol=symbol,interval=interval,limit=limit)
    df = pd.DataFrame()
    for candle_inx in range(limit):
        datetime = dt.datetime.fromtimestamp(klines[candle_inx][0] / 1e3)
        close_price = float(klines[candle_inx][4])
        new_df = pd.DataFrame({'Time': [datetime], f'{symbol}':[close_price]})
        df = pd.concat([df, new_df],)
    df.to_csv('new_prices.csv')
    return df

def count_delta(limit = 60 ,symbol ='ETHUSDT' , delta=0.01,):
    data = get_binanceklines(symbol='ETHUSDT', limit = limit)
    max_price = data[symbol].max()
    min_price = data[symbol].min()
    price_change = (max_price-min_price)/min_price
    #r_square = 0.63, значит 63 процента изменений цены эфира зависит от изменений цены биткоина,
    #чистых независящих значений 1- 0.63=0.37.пропорция:  0.37(price_change) >= 0.01, price_change:
    cleared_price_change  =  delta / (1 - r_squared)
    return True if price_change >= cleared_price_change else False

def logging_changes(symbol='ETHUSDT', limit=60):
    while True:
        time.sleep(limit)
        if count_delta (limit = limit, symbol = symbol):
            print(f"За час цена {symbol} изменилась на 1%")
        else:
            print(f'За час изменений цены {symbol} более, чем на 1% не было')


if __name__ == '__main__':
    count_delta() # сразу берем значения за последний час
    logging_changes(limit=60)