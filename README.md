# How to use helicone proxy server using different method.

## Description

This repository demonstrates to how to use helicone proxy server with methods like cURL, Lang chain, and Chat completion helps us understand how well it works.

**Helicone proxy server link**: `https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/v1`


## Prerequisite

  ### Required modules:-
  `pip install langchain`<br/>
  `pip install openai`<br/>
  
  ### Required Information:-
  1.  openai.api_type - we use azure openai key so we need set as "azure"
  2.  openai.api_version - It specifies the version of the Azure OpenAI API
  3.  openai.api_base - i.e.  Helicone proxy server Link
  4.  Helicone User Id - User Name
  5.  engine - It specify the Azure OpenAI engine
  6.  model_name - It specifies the specific model within the chosen engine
  7.  temperature - It controls the randomness of the generated text.



## How to run :-

Step-by-step user guide [Video](https://drive.google.com/file/d/1eirDH9N04ydhHLL0a_MtdmFAp-TjphLq/view?usp=sharing)

1. Run the below command to clone this repo:
```
git clone https://github.com/abhisheksrivastav3604/how-to-use-helicone-proxy-server-2.0.git
```
2. For cURL method :
   ```
   --request POST \
   --url `https://3ktbkv6m9d.execute-api.ap-south-1.amazonaws.com/dev/request/<engine name>/v1/chat`
   --header `User-Id: <User-name>` \
   --data `{
	"model": "gpt-4",
	"temperature": 0.5,
	"messages": [
		{
			"role": "user",
			"content": "Hii"
		}
	  ]
        }'
   ```
3. For Langchain prompt method :
   ```
   you have to run this command in your terminal `proxy_server_test.py`
   ```
4. For Langchain agent method :
   ```
   you have to run this command in your terminal `test_agent.py`
   ```
5. For ChatCompletion method :
   ```
   you have to run this command in your terminal `chatcomp.py`
   ```
   


