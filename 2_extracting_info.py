# extracting_info_from_email.py

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-08-01-preview"
)

# Select the General Purpose curie model for text
model = os.getenv("CHAT_COMPLETION_NAME")

email_content = """

Dear customer service,

I lost my invoice. Can you please resend it? My customer account number is 12567 and the invoice number is 3443.

Best regards,
Thomas

"""


class ExtractedEmail(BaseModel):
    customer_number: str
    invoice_number: str



completion = client.beta.chat.completions.parse(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You will receive an email and from this email you extract the customer number and the invoice number",
        },
        {
            "role": "user",
            "content": """
            Extract customer number and invoice number from this email
            
            
            """+email_content,
        },
    ],
    response_format=ExtractedEmail,
)

message = completion.choices[0].message

if message.parsed:
    print("Customer number: "+message.parsed.customer_number)
    print("Invoice number: "+message.parsed.invoice_number)

else:
    print(message.refusal)