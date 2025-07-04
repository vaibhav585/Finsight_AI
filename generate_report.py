from top_gainers import get_top_stocks
from news_fetcher import fetch_news
from granite_summarizer import summarize_company_news  # ✅ Correct import


def generate_daily_summary():
    report_lines = []
    top_stocks = get_top_stocks()

    for stock in top_stocks:
        symbol = stock['symbol']
        change = stock['change']
        print(f"\n🔍 Fetching news for {symbol}...")

        articles = fetch_news(symbol)

        # ✅ FIXED: Call with both company name and articles
        summary = summarize_company_news(symbol, articles)

        entry = f"\n📈 **{symbol}** – {change}%\n{summary}\n"
        report_lines.append(entry)

    return "\n".join(report_lines)

# 🧪 Run this only for CLI test, not inside Flask
if __name__ == "__main__":
    final_report = generate_daily_summary()
    print("\n===== 📊 Daily Financial Summary =====\n")
    print(final_report)