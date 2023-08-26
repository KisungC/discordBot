import os
import openai
from dotenv import load_dotenv

openai.api_key = os.getenv('ai_api_key')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a programming teacher. Only help by giving relavent examples and explanation; do not give the direct answer."},
    {"role": "user", "content": "how can I get better at coding"}
  ]
)

# def process_file(content):
# pass in content, have chatgpt read over, let chatgpt know that this file is a note from the prof. only use this context to help students

# def give_explanation(question):
# pass in the question for chatgpt to answer

print(completion.choices[0].message.content)