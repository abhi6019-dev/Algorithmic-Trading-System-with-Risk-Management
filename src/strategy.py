import pandas as pd
import numpy as np

def generate_signals(df):
    df = df.copy()

    # --- Initialize Signal ---
    df["Signal"] = 0

    # --- STRATEGY RULES ---

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