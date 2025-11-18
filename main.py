# main.py
from config import SP500_TICKER, SECTOR_ETF_FOR_STOCK
from data_loader import download_prices
from returns import compute_returns
from stats import compute_beta_and_stats, correlation_table
from plotting import plot_beta_scatter

def run_beta_calculator(stock_ticker, sector_ticker=None, start="2023-01-01", end="2024-01-01"):
    if sector_ticker is None:
        sector_ticker = SECTOR_ETF_FOR_STOCK.get(stock_ticker)

    tickers = [stock_ticker, SP500_TICKER]
    if sector_ticker:
        tickers.append(sector_ticker)

    prices = download_prices(tickers, start, end)
    prices.columns = tickers

    returns = compute_returns(prices, use_log=True)

    stock_ret = returns[stock_ticker]
    mkt_ret = returns[SP500_TICKER]
    sector_ret = returns[sector_ticker] if sector_ticker else None

    # Stock vs Market
    stats_mkt = compute_beta_and_stats(stock_ret, mkt_ret)
    print(f"\n=== {stock_ticker} vs S&P 500 ({SP500_TICKER}) ===")
    for k, v in stats_mkt.items():
        print(f"{k}: {v:.6f}")

    plot_beta_scatter(stock_ret, mkt_ret, title=f"{stock_ticker} vs S&P 500 beta")

    # Stock vs Sector
    if sector_ret is not None:
        stats_sector = compute_beta_and_stats(stock_ret, sector_ret)
        print(f"\n=== {stock_ticker} vs Sector ETF ({sector_ticker}) ===")
        for k, v in stats_sector.items():
            print(f"{k}: {v:.6f}")

        plot_beta_scatter(stock_ret, sector_ret, title=f"{stock_ticker} vs Sector ETF ({sector_ticker}) beta")

    # Correlation table
    cols = [stock_ticker, SP500_TICKER]
    if sector_ticker:
        cols.append(sector_ticker)

    corr_tab = correlation_table(returns[cols])
    print("\n=== Correlation Table ===")
    print(corr_tab)


if __name__ == "__main__":
    stock = "AAPL"
    sector = "XLK"
    run_beta_calculator(stock_ticker=stock, sector_ticker=sector, start="2020-01-01", end="2025-01-01")
