import pandas as pd

def add_indicator(df):
    df["Close"] = df["Close"].squeeze()

        # --- Moving Averages ---
    df["MA_20"] = df["Close"].rolling(20).mean()
    df["MA_50"] = df["Close"].rolling(50).mean()

    # --- Z-Score (mean reversion) ---
    df["STD_20"] = df["Close"].rolling(20).std()
    df["Z"] = (df["Close"] - df["MA_20"]) / df["STD_20"]

    # --- ATR (volatility) ---
    high_low = df["High"] - df["Low"]
    high_close = (df["High"] - df["Close"].shift()).abs()
    low_close = (df["Low"] - df["Close"].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df["ATR_14"] = tr.rolling(14).mean()

    # --- Trend regime ---
    df["Trend"] = (df["MA_20"] > df["MA_50"]).astype(int)

    return df
