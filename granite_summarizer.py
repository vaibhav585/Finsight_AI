import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Import integration clients
from llm_utils.integrations_example import WatsonxClient, HuggingFaceSummarizer

# Initialize clients (can be None if not configured)
try:
    watsonx_client = WatsonxClient()
except Exception:
    watsonx_client = None

try:
    huggingface_summarizer = HuggingFaceSummarizer()
except Exception:
    huggingface_summarizer = None

def summarize_company_news(company_name, articles, method="nltk"):
    """
    Summarize company news articles using the specified method.
    method: "nltk" (default), "watsonx", or "huggingface"
    """
    # Combine all article texts
    texts = []
    for article in articles:
        text = article.get("title", "")
        if article.get("description"):
            text += " " + article["description"]
        texts.append(text)
    combined_text = " ".join(texts)

    # Truncate combined_text to 1000 characters to avoid pipeline issues
    if len(combined_text) > 1000:
        combined_text = combined_text[:1000]
        print("Truncated combined_text to 1000 characters for summarization.")

    if method == "watsonx" and watsonx_client:
        try:
            return watsonx_client.summarize_text(combined_text)
        except Exception as e:
            print(f"Watsonx summarization failed: {e}")
            # fallback to nltk

    if method == "huggingface" and huggingface_summarizer:
        try:
            print("Calling HuggingFace summarizer...")
            summary = huggingface_summarizer.summarize_text(combined_text)
            print(f"HuggingFace summary: {summary}")
            return summary
        except Exception as e:
            print(f"HuggingFace summarization failed: {e}")
            # fallback to nltk

    # Default nltk summarization
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(combined_text)
    tokens = [token for token in tokens if token.lower() not in stop_words]
    return " ".join(tokens)
