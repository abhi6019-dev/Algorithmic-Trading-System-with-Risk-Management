from src.data_loader import load_data
from src.indicators import add_indicator
from src.visualization import plot_results

def main():
    data = load_data("^NSEI","2024-01-01","2025-01-01")
    data = add_indicator(data,20)
    plot_results(data)


if __name__ == "__main__":
    main()