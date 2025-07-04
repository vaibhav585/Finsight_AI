import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
def summarize_company_news(company_name, articles):
    stop_words = set(stopwords.words('english'))
    summary = []
    for article in articles:
        text = article["title"]
        if article["description"] is not None:
            text += " " + article["description"]
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in stop_words]
        summary.append(" ".join(tokens))
    return " ".join(summary)