import yfinance as yf

def load_data(symbol, start, end):
    #loads data accordingly
    df = yf.download(symbol, start, end)
    df.columns = df.columns.get_level_values(0)
    return df