from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from textblob import TextBlob
import nltk
import logging

# Downloading the punkt tokenizer
if not nltk.data.find('tokenizers/punkt'):
    try:
        nltk.download('punkt')
    except LookupError:
        nltk.download('punkt')

app = FastAPI()

class TextInput(BaseModel):
    text: str

    @field_validator('text')
    @classmethod
    def check_text_not_empty(cls, value: str) -> str:
        if len(value) == 0:
            raise ValueError('Text must not be empty')
        return value

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_sentiment(text: str) -> str:
    # Analyzing text sentiment using TextBlob

    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = new_func(sentiment)
    logger.info(f"Sentiment polarity: {polarity}")

    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

def new_func(sentiment):
    polarity = sentiment.polarity
    return polarity

@app.post('/analyze')
def analyze(text_input: TextInput):
    # Endpoint to analyze the sentiment of a given text

    try:
        sentiment = analyze_sentiment(text_input.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")
    
    return {
    "text": text_input.text,
    "sentiment": sentiment,
    "message": f"This text is {sentiment.lower()}"
    }
