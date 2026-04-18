import pandas as pd

def add_indicator(df, window):
    df["MA"] = df['Close'].rolling(window=window).mean()
    df["STD"] = df['Close'].rolling(window=window).std()
    df["STD"] = df["STD"].replace(0, 1)
    df["Close"] = df["Close"].squeeze()

    df["Z_Score"] = (df["Close"] - df["MA"]) / df["STD"]
    return df
