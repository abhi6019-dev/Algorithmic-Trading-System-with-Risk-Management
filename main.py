from src.data_loader import load_data
from src.indicators import add_indicator
from src.visualization import plot_results
from src.strategy import generate_signals
from src.backtest import run_backtest
def main():
    data = load_data("AAPL", "2015-01-01", "2025-01-01")

    data = add_indicator(data, 20)   # if you already have it
    data = generate_signals(data)

    data = run_backtest(data, 10000)

    print(data["Portfolio_Value"].iloc[-1])

    print(data[["Close","Signal", "Portfolio_Value"]])
    plot_results(data)

if __name__ == "__main__":
    main()