import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime

from pycoingecko import CoinGeckoAPI


class CryptoData:
    def __init__(self):
        self.price = None
        self.date = None
        self.cg = CoinGeckoAPI()

    def get_data(self, id='bitcoin', vs_currency='usd', days='1', plot=False):
        tmp = self.cg.get_coin_market_chart_by_id(id, vs_currency, days)
        self.price = np.array(tmp['prices'])[:, 1]
        self.date = [datetime.datetime.fromtimestamp(item / 1000) for item in np.array(tmp['prices'])[:, 0]]
        if plot:
            plt.plot_date(self.date, self.price,'-')
            plt.show()
