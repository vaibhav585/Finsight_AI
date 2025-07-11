# FinSightAI

**FinSightAI** is an AI-powered financial assistant that leverages the latest advances in Generative AI (LLMs + NLP) to:

- Summarize daily financial news
- Analyze sentiment of company-related articles
- Predict short-term stock trends based on news and price data
- Provide relevant stock information about the company

---

## Technologies Used

| Feature                     | Tools/Technologies                                                                                   |
|-----------------------------|----------------------------------------------------------------------------------------------------|
| LLMs & NLP                  | HuggingFace Transformers (actively used), IBM Watsonx (planned, not yet implemented)               |
| Backend                     | Python, Flask                                                                                       |
| Financial APIs              | Yahoo Finance (`yfinance`), NewsAPI, Alpha Vantage                                                 |
| Data Processing & Utilities | pandas, requests, beautifulsoup4, python-dotenv                                                    |
| Charts & Visualization      | Plotly, Matplotlib                                                                                  |
| AI APIs                     | OpenAI                                                                                            |
| Deployment                  | IBM Cloud (planned)                                                                                |
| Version Control             | Git + GitHub                                                                                       |

Note: The `llm_utils` directory contains example integration code for IBM Watsonx and HuggingFace Transformers.

---

## Installation

```bash
git clone https://github.com/vaibhav585/FinSight_AI.git
cd FinSight_AI
pip install -r requirements.txt
```

---

## Usage

Run the Flask application:

```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000` to access the FinSightAI web interface.

---

## Project Structure

- `app.py`: Main Flask application handling user input and displaying financial data and news
- `granite_summarizer.py`: Summarizes company news using NLP techniques (NLTK)
- `newsfetcher.py`: Fetches news articles related to stocks using NewsAPI
- `top_gainers.py`: Retrieves top stock gainers using Yahoo Finance
- `generate_report.py`: Generates textual daily financial summary reports and PDF reports
- `utils.py`: Helper functions for data fetching and processing
- `llm_utils/integrations_example.py`: Example code for integrating IBM Watsonx and HuggingFace Transformers
- `templates/`: HTML templates for the web interface
- `static/`: Static assets like CSS and images
- `requirements.txt`: Python dependencies

---

## License

This project is licensed under the MIT License.
