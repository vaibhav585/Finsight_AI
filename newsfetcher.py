import requests
def fetch_news(company_name):
    api_key = "e5d05e4d54684544976d5a30b3b37634"
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["articles"]