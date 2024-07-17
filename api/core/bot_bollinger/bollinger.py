from datetime import datetime, timedelta
from api.core.connect import client
import talib
import time
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#sleep для получения нулевой секунды
def sleep_to_next_min():
    time_to_sleep = 60 - time.time() % 60 + 2
    print('sleep', time_to_sleep)
    time.sleep(time_to_sleep)

while True:
    sleep_to_next_min()
    klines = client.get_kline(symbol='NOTUSDT', interval=5, limit=100)
    klines = klines['result']['list']
    close_prices = [float(i[4]) for i in klines]
    close_prices_np = np.array(close_prices)
    close_prices_np = close_prices_np[::-1]

    upper_band, middle_band, lower_band = talib.BBANDS(close_prices_np, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

    bollinger_df = pd.DataFrame({
        'Close': close_prices_np,
        'Upper Band': upper_band,
        'Middle Band': middle_band,
        'Lower Band': lower_band
    })

    plt.figure(figsize=(12, 6))
    plt.plot(close_prices_np, label='close prices')
    plt.plot(upper_band, label='upper band', linestyle='--')
    plt.plot(middle_band, label='middle band', linestyle='--')
    plt.plot(lower_band, label='lower band', linestyle='--')
    plt.title('Bollinger Band for POPCAT')
    plt.legend(loc='best')
    plt.show()

    price = bollinger_df.iloc[-1]['Close']
    ub = bollinger_df.iloc[-1]['Upper Band']
    lb = bollinger_df.iloc[-1]['Lower Band']

    print('Price:', price)
    print('Upper Band:', ub)
    print('Lower Band:', lb)

