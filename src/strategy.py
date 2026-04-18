import pandas as pd
import numpy as np

def generate_signals(df):
    df = df.copy()

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

    # --- Initialize Signal ---
    df["Signal"] = 0

    # --- STRATEGY RULES (RELAXED) ---

    # Trend-following
    trend_buy = (df["Trend"] == 1) & (df["Close"] > df["MA_20"] * 0.995)
    trend_sell = (df["Trend"] == 1) & (df["Close"] < df["MA_20"] * 1.005)

    # Mean-reversion (RELAXED thresholds)
    mr_buy = (df["Trend"] == 0) & (df["Z"] < -0.8)
    mr_sell = (df["Trend"] == 0) & (df["Z"] > 0.8)

    # Apply signals
    df.loc[trend_buy | mr_buy, "Signal"] = 1
    df.loc[trend_sell | mr_sell, "Signal"] = -1

    # ⚠️ Prevent lookahead bias
    df["Signal"] = df["Signal"].shift(1).fillna(0)

    return df