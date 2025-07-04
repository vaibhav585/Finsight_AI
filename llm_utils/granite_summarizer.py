## 1️⃣ Import required libraries
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParams
from dotenv import load_dotenv
import os

# 2️⃣ Load environment variables
load_dotenv()

# 3️⃣ Read Watson credentials
api_key = os.getenv("WATSON_API_KEY")
url = os.getenv("WATSON_URL")
project_id = os.getenv("PROJECT_ID")

# 4️⃣ Set model parameters
params = GenTextParams(
    decoding_method="greedy",
    max_new_tokens=300
)

# 5️⃣ Load Granite model
model = Model(
    model_id="granite-13b-instruct-v2",
    params=params,
    credentials={"url": url, "apikey": api_key},
    project_id=project_id,
)

# 6️⃣ Function to summarize multiple news items
def summarize_company_news(company_name, articles):
    combined_text = "\n\n".join(articles)
    prompt = f"""Summarize all the recent news for {company_name}:

{combined_text}

Summary:"""

    try:
        response = model.generate(prompt)
        return response['results'][0]['generated_text'].strip()
    except Exception as e:
        return f"Error from Granite model: {e}"
