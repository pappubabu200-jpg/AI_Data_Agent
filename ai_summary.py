import openai
from config import MODE, OPENAI_API_KEY

def ai_summary(text):
    if MODE == "DEV":
        return "This is a dummy AI summary for development purposes."
    openai.api_key = OPENAI_API_KEY
    prompt = f"Summarize this data concisely and clearly for a bookstore owner:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
