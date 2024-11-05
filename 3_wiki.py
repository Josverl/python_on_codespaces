import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import requests

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-08-01-preview"
)

# Select the General Purpose curie model for text
model = os.getenv("CHAT_COMPLETION_NAME")


url = "https://en.wikipedia.org/wiki/Benjamin_Franklin"



response = requests.get(url)



class Person(BaseModel):
    name: str
    occupation: str
    related_persons: list["Person"]




completion = client.beta.chat.completions.parse(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You extract information from the provided HTML page and provide the requested fields",
        },
        {
            "role": "user",
            "content": """
            Extract the name, occupation and related persons from this data
            
            
            """+response.text[:400_000],
        },
    ],
    response_format=Person,
)

message = completion.choices[0].message

if message.parsed:
    print("Name: "+message.parsed.name)
    print("Occupation: "+message.parsed.occupation)

    print(f"== Related persons  [{len(message.parsed.related_persons)}] ==")
    
    for related_person in message.parsed.related_persons:
        print(f"- {related_person.name} ({related_person.occupation})")

else:
    print(message.refusal)