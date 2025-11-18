# stats.py
import pandas as pd

def compute_beta_and_stats(stock_ret, benchmark_ret):
    df = pd.concat([stock_ret, benchmark_ret], axis=1, join="inner").dropna()
    s = df.iloc[:, 0]
    m = df.iloc[:, 1]

    mean_stock = s.mean()
    mean_bench = m.mean()

    vol_stock = s.std()
    vol_bench = m.std()

    cov_sm = s.cov(m)
    var_m = m.var()
    beta = cov_sm / var_m

    corr = s.corr(m)
    R2 = corr ** 2

    return {
        "mean_stock": mean_stock,
        "mean_bench": mean_bench,
        "vol_stock": vol_stock,
        "vol_bench": vol_bench,
        "cov_sm": cov_sm,
        "var_m": var_m,
        "beta": beta,
        "corr": corr,
        "R2": R2,
    }

def correlation_table(returns_df):
    return returns_df.corr()
