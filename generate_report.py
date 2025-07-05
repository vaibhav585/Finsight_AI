from top_gainers import get_top_stocks
from newsfetcher import fetch_news
from granite_summarizer import summarize_company_news  # ✅ Correct import
from fpdf import FPDF


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


def generate_pdf_report(filename="FinSightAI_Project_Report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "FinSightAI Project Report", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "1. Project Overview", ln=True)
    pdf.set_font("Arial", '', 11)
    overview_text = (
        "FinSightAI is an AI-powered financial assistant leveraging the latest advances in Generative AI (LLMs + NLP) to:\n"
        "- Summarize daily financial news\n"
        "- Analyze sentiment of company-related articles\n"
        "- Predict short-term stock trends based on news and price data\n"
        "- Provide relevant stock information about companies\n"
    )
    pdf.multi_cell(0, 8, overview_text)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "2. Technologies Used", ln=True)
    pdf.set_font("Arial", '', 11)
    tech_text = (
        "- LLMs & NLP: IBM Watsonx, HuggingFace Transformers\n"
        "- Backend: Python, Flask\n"
        "- Financial APIs: Yahoo Finance (yfinance), NewsAPI\n"
        "- Charts & Visualization: Plotly, Matplotlib\n"
        "- Deployment: IBM Cloud\n"
        "- Version Control: Git + GitHub\n"
    )
    pdf.multi_cell(0, 8, tech_text)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "3. Core Modules and Functionality", ln=True)
    pdf.set_font("Arial", '', 11)
    modules_text = (
        "- app.py: Main Flask web application handling user input and displaying financial data and news\n"
        "- granite_summarizer.py: Summarizes company news using NLP techniques\n"
        "- newsfetcher.py: Fetches news articles related to stocks\n"
        "- top_gainers.py: Retrieves top stock gainers\n"
        "- generate_report.py: Generates textual daily financial summary reports\n"
        "- utils.py: Helper functions for data fetching and processing\n"
    )
    pdf.multi_cell(0, 8, modules_text)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "4. Sample Daily Financial Summary Report", ln=True)
    pdf.set_font("Arial", '', 11)
    summary = generate_daily_summary()
    pdf.multi_cell(0, 8, summary)

    pdf.output(filename)
    print(f"PDF report generated: {filename}")


# 🧪 Run this only for CLI test, not inside Flask
if __name__ == "__main__":
    generate_pdf_report()
