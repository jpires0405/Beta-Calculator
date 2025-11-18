# plotting.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_beta_scatter(stock_ret, benchmark_ret, title="Stock vs Benchmark"):
    df = pd.concat([benchmark_ret, stock_ret], axis=1, join="inner").dropna()
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    b, a = np.polyfit(x, y, 1)

    plt.figure()
    plt.scatter(x, y, alpha=0.4, label="Daily returns")
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = a + b * x_line
    plt.plot(x_line, y_line, label=f"Fit line (beta ≈ {b:.2f})")
    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)
    plt.title(title)
    plt.xlabel("Benchmark returns")
    plt.ylabel("Stock returns")
    plt.legend()
    plt.tight_layout()
    plt.show()

