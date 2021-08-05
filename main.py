import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime

from pycoingecko import CoinGeckoAPI

if __name__ == "__main__":
    cg = CoinGeckoAPI()
    a7 = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days='90')
    p7 = np.array(a7['prices'])[:, 0]
    b7 = np.array(a7['prices'])[:, 1]
    p7d = [datetime.datetime.fromtimestamp(item / 1000) for item in p7]
    plt.plot_date(p7d, b7, '-')
    plt.show()
    print('hello world')