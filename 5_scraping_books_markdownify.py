import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import requests
from typing import Optional
import json
import pandas as pd
import markdownify

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-08-01-preview"
)

# Select the General Purpose curie model for text
model = os.getenv("CHAT_COMPLETION_NAME")


url = "https://books.toscrape.com/"



response = requests.get(url)


class BookDetails(BaseModel):
    title: str
    price: float
    availability: str
    rating: Optional[str]

class BookPage(BaseModel):
    books: list[BookDetails]
    category: Optional[str]
    next_page_url: Optional[str]




completion = client.beta.chat.completions.parse(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You extract books from a HTML webpage",
        },
        {
            "role": "user",
            "content": """
            Extract the requested data about these books
            
            
            """+markdownify.markdownify(response.text),
        },
    ],
    response_format=BookPage,
)

message = completion.choices[0].message

if message.parsed:

    json_output = json.dumps([book.model_dump() for book in message.parsed.books], indent=4)

    books = json.loads(json_output)

    all_books = []

    for book in books:
        all_books.append(book)



    df = pd.DataFrame(all_books)
    df.to_excel("books.xlsx",index=False)
    df.to_csv("books.csv",index=False)

    print(f" {len(df)} Books extracted and saved to books.xlsx and books.csv")

else:
    print(message.refusal)