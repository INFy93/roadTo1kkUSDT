#coins data
import pprint
import json
from datetime import datetime, timedelta
from api.core.connect import client


def getKlineData(coin='POPCATUSDT'):
    now = round(datetime.now().timestamp()) * 1000
    hour_ago = datetime.now() - timedelta(hours=1)
    hour_ago = round(hour_ago.timestamp()) * 1000

    # get kline data. interval - 5min, period - last hour
    mark_price = client.get_mark_price_kline(symbol=coin, interval=5, start=hour_ago, end=now)
    mark_price_better_view = mark_price['result']['list'][::-1]

    #create array for input
    timestamps = []
    kline_data = []
    for i in range(len(mark_price_better_view) - 1):
        temp = float(mark_price_better_view[i][0])
        temp_better = temp / 1000
        timestamp = datetime.fromtimestamp(int(temp_better)).strftime('%H:%M')
        timestamps.append(timestamp)
        kline_data.append(float(mark_price_better_view[i][4]))

    # detecting short-time trend
    last_index = len(mark_price_better_view) - 1
    first_value = float(mark_price_better_view[0][4])
    last_value = float(mark_price_better_view[last_index][4])
    trend_up = first_value < last_value
    trend_down = first_value > last_value

    # calculate difference between prices of first and last kline
    diff = last_value - first_value

    # conditions for trend
    current_trend = ''
    if trend_up:
        current_trend = 'Восходящий'
    elif trend_down:
        current_trend = 'Нисходящий'
    else:
        current_trend = 'WTF'

    result = dict()
    result['timestamps'] = timestamps
    result['kline_data'] = kline_data
    result['current_trend'] = current_trend

    return result
