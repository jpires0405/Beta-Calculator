# returns.py
import numpy as np

def compute_returns(prices, use_log=True):
    if use_log:
        rets = np.log(prices / prices.shift(1))
    else:
        rets = prices.pct_change()
    return rets.dropna()
