from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
import nltk

if not nltk.data.find('tokenizers/punkt'):
    nltk.download('punkt')

app = FastAPI()

class TextInput(BaseModel):
    text: str

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity #type: ignore
    print(f"Polarity: {polarity}")

    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

@app.post('/analyze')
def analyze(text_input: TextInput):
    sentiment = analyze_sentiment(text_input.text)
    return {'text': text_input.text, 'sentiment': sentiment}
