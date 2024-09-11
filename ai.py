import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


messages = [{"role": "user", "content": "What is the capital of New York?"}]
try:
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages,
    temperature=0)

    print(response.choices[0].message.content)
except Exception as e:
    print(e)