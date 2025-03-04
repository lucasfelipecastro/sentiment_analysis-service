from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
import nltk

nltk.download('punkt')
app = FastAPI()