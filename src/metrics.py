import numpy as np

def calculate_returns(df):
    df["Returns"] = df["Portfolio_Value"].pct_change()
    return df


def total_return(df):
    return (df["Portfolio_Value"].iloc[-1] / df["Portfolio_Value"].iloc[0]) - 1


def cagr(df):
    n = len(df)
    return (df["Portfolio_Value"].iloc[-1] / df["Portfolio_Value"].iloc[0]) ** (252 / n) - 1


def sharpe_ratio(df, risk_free_rate=0):
    returns = df["Returns"].dropna()
    return (returns.mean() - risk_free_rate) / (returns.std() + 1e-9) * np.sqrt(252)


def max_drawdown(df):
    equity = df["Portfolio_Value"]
    peak = equity.cummax()
    drawdown = (equity - peak) / peak
    return drawdown.min()


def win_rate(df):
    returns = df["Returns"].dropna()
    wins = (returns > 0).sum()
    return wins / len(returns)

def volatility(df):
    return df["Returns"].std() * np.sqrt(252);