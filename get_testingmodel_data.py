
from binance import Client
import pandas as pd
from config import API_TOKEN, SECRET_KEY

client = Client(API_TOKEN, SECRET_KEY)

def get_price_crypto(currency):
    historic_klines = client.get_klines(symbol=currency, interval="1d", limit=1000)
    df = pd.DataFrame()
    for candle in range(len(historic_klines)):
        open_price = float(historic_klines[candle][1])
        highest_price = float(historic_klines[candle][2])
        close_price = float(historic_klines[candle][4])
        new_df = pd.DataFrame({'Highest': [highest_price], 'Open': [open_price], 'Close': [close_price]})
        df = pd.concat([df, new_df])
    return df


eth_df = get_price_crypto("ETHUSDT")
eth_df.to_csv('ETH.csv')
btc_df = get_price_crypto('BTCUSDT')
btc_df.to_csv('BTC.csv')

correlation_cofficient = eth_df.corrwith(btc_df) #Highest - 0.795048 Open  - 0.796746 Close - 0.796338
r_squared = correlation_cofficient["Close"] ** 2 #проверяем значения среднеквадратичного отклонения, сходится ли с графиком
#R_SQUARED = 0.63

