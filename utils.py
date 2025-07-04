import yfinance as yf
from newsfetcher import fetch_news
from granite_summarizer import summarize_company_news
def parallel_fetch(company_name):
    ticker = yf.Ticker(company_name)
    news = fetch_news(company_name)
    info = ticker.info
    hist = ticker.history(period="5y")
    summary = summarize_company_news(company_name, news)
    return news, info, hist, summary