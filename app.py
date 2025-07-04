from flask import Flask, render_template, request
import yfinance as yf
from newsapi import NewsApiClient
app = Flask(__name__)
# Initialize news API client
news_api_client = NewsApiClient(api_key='e5d05e4d54684544976d5a30b3b37634')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        
        if not company_name:
            return render_template('index.html', error="Please enter a company name")
            
        try:
            ticker = yf.Ticker(company_name)
            info = ticker.info
            
            # Prepare comprehensive financial data
            financials = {
                'basic': {
                    'name': info.get('shortName', 'N/A'),
                    'sector': info.get('sector', 'N/A'),
                    'industry': info.get('industry', 'N/A')
                     },
                'valuation': {
                    'market_cap': format_money(info.get('marketCap')),
                    'pe_ratio': format_number(info.get('trailingPE'))
                },
                'performance': {
                    'revenue_ly': format_money(info.get('totalRevenue')),
                    'earnings_ly': format_money(info.get('netIncomeToCommon')),
                    'profit_margin': format_percent(info.get('profitMargins'))
                }
            }
            
            # Get relevant news (max 5 articles)
            news_results = news_api_client.get_everything(
                q=f"{financials['basic']['name']} stock",
                language='en',
                sort_by='publishedAt',
                page_size=5
            )
            
            return render_template(
                'result.html',
                financials=financials,
                company=company_name.upper(),
                articles=news_results.get('articles', []),
                currency=info.get('currency', 'USD')
            )
        except Exception as e:
            return render_template('error.html', error=str(e))
            
    return render_template('index.html')
# Helper formatting methods
def format_money(value):
    if value is None: return "N/A"
    return "${:,.2f}".format(value / 10**9) + "B" if value >= 10**9 else "${:,.2f}M".format(value / 10**6)
def format_number(value):
    return "N/A" if value is None else "{:,.2f}".format(value)
def format_percent(value):
    return "N/A" if value is None else "{:.2%}".format(value)
if __name__ == '__main__':
    app.run(debug=True)