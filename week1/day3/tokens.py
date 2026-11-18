import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model_name = "openai/gpt-oss-20b"
role="user"
# prompt="what is java"
prompt1="hi!"
prompt2="what is space science?"
prompt3="what is visor 1 and visor 2?"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model_name, messages=messages, max_tokens=500)
    usage = response.usage
    print(f"prompt: {prompt} --> your token: {usage.prompt_tokens} completion token: {usage.completion_tokens} total tokens: {usage.total_tokens} finish reason:{response.choices[0].finish_reason}")




# message_system ={
#     "role":"system",
#     "content":"you are a brand manager who is an expert in naming . name should be in one word and only one name"
# }

# messages=[message_system, message]
# response = client.chat.completions.create(model=model_name , messages=messages, temperature=2)
# # print(response)

# print("---------------------------------------------------")
# print(response.choices[0].message.content)