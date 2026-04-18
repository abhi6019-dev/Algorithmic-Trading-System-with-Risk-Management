def run_backtest(df, initial_capital=10000):
    df = df.copy()

    capital = initial_capital
    position = 0   # 0 = no position, 1 = holding
    shares = 0

    portfolio_values = []

    for i in range(len(df)):
        price = df["Close"].iloc[i]
        signal = df["Signal"].iloc[i]

        # --- BUY ---
        if signal == 1 and position == 0:
            shares = max(1, int(capital // price))  # FIX: ensures at least 1 share
            capital -= shares * price
            position = 1
            print(f"BUY at {price}, shares={shares}")

        # --- SELL ---
        elif signal == -1 and position == 1:
            capital += shares * price
            shares = 0
            position = 0
            print(f"SELL at {price}")

        # --- Portfolio Value ---
        total_value = capital + shares * price
        portfolio_values.append(total_value)

    df["Portfolio_Value"] = portfolio_values

    return df