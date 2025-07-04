import yfinance as yf
def get_top_stocks():
    ticker = yf.Ticker("^GSPC")
    data = ticker.history(period="1d")
    top_gainers = data["Close"].sort_values(ascending=False).head(10)
    return top_gainers.index.tolist()