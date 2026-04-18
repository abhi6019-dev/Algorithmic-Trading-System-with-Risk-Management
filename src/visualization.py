import matplotlib.pyplot as plt
import os 

def  plot_results(df):
    plt.figure(figsize=(15, 8))
    plt.plot(df.index, df['Close'], label='Nifty 50 Close Price', color='blue')
    plt.plot(df.index, df['MA'], label='Moving Average',linestyle='--', color='red')
    plt.title("Nifty 50 Stock Prices")
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.grid(True)

    plt.savefig('outputs/charts/plot.png')