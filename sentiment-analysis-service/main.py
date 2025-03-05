from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from textblob import TextBlob
import nltk

# Downloading the punkt tokenizer
if not nltk.data.find('tokenizers/punkt'):
    nltk.download('punkt')

app = FastAPI()

class TextInput(BaseModel):
    text: str

    @field_validator('text')
    def check_text_not_empty(cls, value):
        if len(value) == 0:
            raise ValueError('Text must not be empty')
        return value
        
def analyze_sentiment(text: str) -> str:
    # Analyzing text sentiment using TextBlob
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
    # Endpoint to analyze the sentiment of a given text
    sentiment = analyze_sentiment(text_input.text)
    return {'text': text_input.text, 'sentiment': sentiment}
