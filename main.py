from src.data_loader import load_data
from src.indicators import add_indicator
from src.visualization import plot_results
from src.strategy import generate_signals
from src.backtest import run_backtest
from src.metrics import *

def main():
    data = load_data("AAPL", "2015-01-01", "2025-01-01")

    data = add_indicator(data)
    data = generate_signals(data)

    data = run_backtest(data)

    print(data["Portfolio_Value"].iloc[-1])

    print(data[["Close","Signal", "Portfolio_Value"]])
    plot_results(data)

    data = calculate_returns(data)

    print("\n📊 PERFORMANCE METRICS")
    print("Total Return:", total_return(data))
    print("CAGR:", cagr(data))
    print("Sharpe Ratio:", sharpe_ratio(data))
    print("Max Drawdown:", max_drawdown(data))
    print("Win Rate:", win_rate(data))
    print("Votality:", volatility(data))

if __name__ == "__main__":
    main()