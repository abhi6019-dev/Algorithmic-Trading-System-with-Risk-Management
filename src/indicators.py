import pandas as pd

def add_indicator(df, window):
    df["MA"] = df['Close'].rolling(window=window).mean()
    return df
