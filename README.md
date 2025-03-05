# Sentiment Analysis API

This project is a simple API built with **FastAPI** that performs sentiment analysis on a given text. The API uses the **TextBlob** library to determine whether the sentiment of the text is positive, negative, or neutral. 

The API is available at the `/analyze` endpoint and accepts a request body with a text to be analyzed.

## Features
- Sentiment analysis based on the polarity of the text.
- Response with sentiment classification (Positive, Negative, or Neutral).
- Input validation to ensure that the text is not empty.

## Technologies
- **FastAPI**: Framework for creating fast and efficient APIs.
- **Pydantic**: Data validation for API inputs and outputs.
- **TextBlob**: Library for sentiment analysis and text processing.
- **nltk**: Library for natural language processing.

## Installation

### 1. Clone the repository
Clone this repository to your local environment:

```bash
git clone github.com/lucasfelipecastro/sentiment_analysis-service.git
cd sentiment_analysis-service
```
### 2. Create a virtual environment
To ensure dependencies are isolated, create and activate a virtual environment:
```bash
  python -m venv .venv

  # Activate on Windows
  .venv\Scripts\activate

  # Activate on MacOS/Linux
  source .venv/bin/activate
```
### 3. Install dependencies
Install the necessary dependencies with pip:
```bash
  pip install -r requirements.txt
```
### 4. Run the server
To start the API, run the server with Uvicorn:
```bash
uvicorn main:app --reload
```
This will make the API available at http://localhost:8000.

### Usage
Endpoint

    POST /analyze: This endpoint accepts a text and returns the sentiment associated with it.

Example Request
```bash
{
  "text": "I love animals!"
}
```
Example Response
```bash
{
  "text": "I love animals!",
  "sentiment": "Positive",
  "message": "This text is positive"
}
```

### Using Postman to Test the API

Once the server is running, you can interact with it using Postman.

  1. Open Postman.

  2. Set the HTTP method to POST.

  3. In the URL field, enter the following URL:
     http://localhost:8000/analyze

  4. Go to the Body tab and select raw, then set the format to JSON.

  5. Enter the following JSON in the Body section:
      ```bash
      {
      "text": "This is my text."
      }
      ```
  6. Click on the Send button to make the request.

  7. You will receive a response with the sentiment analysis result.

  Example Response from Postman:
  ```bash
    {
    "text": "This is my text.",
    "sentiment": "Neutral",
    "message": "This text is neutral."
    }
  ```
### License
This project is licensed under the MIT License - see the LICENSE file for details.
