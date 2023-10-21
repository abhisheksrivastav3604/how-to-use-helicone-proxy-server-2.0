import openai

openai.api_type  = "azure"
openai.api_version  = "2023-03-15-preview"
openai.api_key  = "dvdffbfgbfb"
openai.api_base = "https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1"

# Create the completion request
output = openai.ChatCompletion.create(
    headers={
        "User-Id": "<User-ID>"
    },
    engine="GPT4-8k",
    messages=[{"role" :"user", "content": "Hii"}],
    model="gpt-3.5-turbo",
    temperature=0.5   
)
print(output.choices[0].message)
