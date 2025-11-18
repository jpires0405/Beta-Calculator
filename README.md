Beta Calculator

A modular Python tool for computing stock beta vs the S&P 500 and sector ETFs.
Includes return calculations, volatility, covariance, R², correlation matrices, and beta visualisations using yfinance, pandas, and matplotlib.

Designed as part of quantitative analysis work for the King’s Capital Quant Team.

Features

Compute beta, R², volatility, covariance, and correlation

Compare a stock against:

the S&P 500

its sector ETF

Download historical data via yfinance

Log or simple return calculation options

Scatter plots with regression line (beta line)

Modular, extensible architecture

Project Structure
BETA_CALCULATOR/
|-- config.py         # Benchmark + sector ETF mappings
|-- data_loader.py    # yfinance market data download
|-- returns.py        # Return calculations
|-- stats.py          # Beta, R², covariance, correlation, volatility
|-- plotting.py       # Visualisations and regression plots
|-- main.py           # Pipeline orchestrator

Installation
pip install -r requirements.txt

Usage

Run from the project root:

python -m BETA_CALCULATOR.main


The default configuration computes beta for AAPL vs the S&P 500 and XLK.
You can change tickers and date ranges inside main.py.

Requirements:

Python 3.10+
pandas
numpy
matplotlib
yfinance
License

Released under the MIT License.
See the LICENSE file for details.
