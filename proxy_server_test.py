import openai
from langchain.llms import AzureOpenAI
import os

openai.api_type  = "azure"
os.environ["OPENAI_API_KEY"]="9fb2f004510099a"
openai.api_version="2023-03-15-preview"
openai.api_base = "https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1"

# Create the completion request
output = AzureOpenAI(
    headers={
        "User-Id": "<User-ID>",  
    },
    engine="GPT4-8k",
    model_name="gpt-3.5-turbo",
    temperature= 0.5
    
)
print(output("Hii"))
