import matplotlib.pyplot as plt
import os 

def  plot_results(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["Portfolio_Value"])
    plt.title("Portfolio Performance")


    plt.savefig('outputs/charts/plot.png')