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
prompt="suggest a name for my clothing shop "

message={
    "role":role,
    "content":prompt
}

message_system ={
    "role":"system",
    "content":"you are a brand manager who is an expert in naming . name should be in one word and only one name"
}

messages=[message_system, message]
response = client.chat.completions.create(model=model_name , messages=messages, temperature=2)
# print(response)

print("---------------------------------------------------")
print(response.choices[0].message.content)