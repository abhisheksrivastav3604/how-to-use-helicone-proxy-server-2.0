from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import AzureOpenAI
import openai
import os


openai.api_type  = "azure"
os.environ["OPENAI_API_KEY"]="9fb2f0045099"
openai.api_version="2023-03-15-preview"
# os.environ["OPENAI_API_VERSION"]="2023-03-15-preview"
openai.api_base = "https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1"

# Create the completion request
llm = AzureOpenAI(
    headers={
        "User-Id": "<User-ID>",
        
    },
    engine="GPT4-8k",
    model_name="gpt-3.5-turbo",
    temperature=0.5
)

tools = load_tools(["llm-math"], llm=llm);
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True);
# respond= agent.run("What is 3+2")
respond= agent.run("circle radius is equal t0 3.2cm What is the area of circle?")
print(respond)


