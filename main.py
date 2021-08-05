import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime
from crypto_data import CryptoData


if __name__ == "__main__":
    data = CryptoData()
    data.get_data(plot=True)
