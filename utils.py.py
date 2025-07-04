import concurrent.futures
import yfinance as yf
def fetch_news(company_name):
    ticker = yf.Ticker(company_name)
    news = ticker.news
    return news
def fetch_stock_info(company_name):
    ticker = yf.Ticker(company_name)
    info = ticker.info
    return info
def parallel_fetch(company_name):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        news_future = executor.submit(fetch_news, company_name)
        stock_info_future = executor.submit(fetch_stock_info, company_name)
        news = news_future.result()
        stock_info = stock_info_future.result()
    return news, stock_info