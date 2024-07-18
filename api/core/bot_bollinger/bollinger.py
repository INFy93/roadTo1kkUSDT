import datetime
from api.core.connect import client
from api.core.settings import symbol, rsi_length, kline_time, rsi_high, rsi_low, deposit_amount
from api.core.orders.orders import make_order_like_zhongli
import talib
import time
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

last_order = None

#sleep для получения нулевой секунды
def sleep_to_next_min():
    time_to_sleep = 60 - time.time() % 60 + 2
    print('sleep', round(time_to_sleep))
    time.sleep(time_to_sleep)


while True:
    sleep_to_next_min()
    klines = client.get_kline(symbol=symbol, interval=kline_time, limit=100)
    klines = klines['result']['list']
    close_prices = [float(i[4]) for i in klines]
    close_prices_np = np.array(close_prices)
    close_prices_np = close_prices_np[::-1]

    upper_band, middle_band, lower_band = talib.BBANDS(close_prices_np, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0) # Боллинджер

    rsi_value = talib.RSI(close_prices_np, timeperiod=rsi_length)[-1] # актуальное значение RSI


    bollinger_df = pd.DataFrame({
        'Close': close_prices_np,
        'Upper Band': upper_band,
        'Middle Band': middle_band,
        'Lower Band': lower_band
    })

    # plt.figure(figsize=(12, 6))
    # plt.plot(close_prices_np, label='close prices')
    # plt.plot(upper_band, label='upper band', linestyle='--')
    # plt.plot(middle_band, label='middle band', linestyle='--')
    # plt.plot(lower_band, label='lower band', linestyle='--')
    # plt.title('Bollinger Band for POPCAT')
    # plt.legend(loc='best')
    # plt.show()

    price = bollinger_df.iloc[-1]['Close']
    ub = bollinger_df.iloc[-1]['Upper Band']
    lb = bollinger_df.iloc[-1]['Lower Band']

    quantity = str(round(deposit_amount / price, 4))

    stopLossLong = round(lb - lb * 0.02, 4)
    stopLossShort = round(ub + ub * 0.02, 4)
    print("----\n")
    print(f"{datetime.datetime.now().strftime('[%d/%m/%Y, %H:%M:%S]')}")
    print('Price:', price)
    print("stopLossLong:", stopLossLong)
    print("stopLossShort:", stopLossShort)
    print('Upper Band:', round(ub, 4))
    print('Middle Band:', round(middle_band[-1], 4))
    print('Lower Band:', round(lb, 4))
    print('RSI:', round(rsi_value, 2))

    if price < lb and rsi_value < rsi_low and last_order != "Long":
        print("Long!")
        make_order_like_zhongli(client, symbol, quantity, "Buy", takeProfit=round(middle_band[-1], 4), stopLoss=stopLossLong)
        last_order = "Long"
    if price > ub and rsi_value > rsi_high and last_order != "Short":
        print("Short!")
        make_order_like_zhongli(client, symbol, quantity, "Sell", takeProfit=round(middle_band[-1], 4), stopLoss=stopLossShort)
        last_order = "Short"
    else:
        print("Нужный сигнал не получен!")
