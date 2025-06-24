from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objs as go
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    chart_url = None
    if request.method == 'POST':
        company = request.form['company']
        summary = f"This is a placeholder summary for {company}. (Integrate LLMs here)"
        chart_url = f"https://finance.yahoo.com/quote/{company}"  # You can later embed Plotly graphs

    return render_template('index.html', summary=summary, chart_url=chart_url)

if __name__ == '__main__':
    app.run(debug=True)
