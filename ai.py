import os
import openai
import main
from dotenv import load_dotenv

openai.api_key = os.getenv('ai_api_key')



def send_data_ai(content, question):
  global userMessage, userQuestion
  userMessage = content
  userQuestion = question
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a programming teacher. Only help by giving relavent examples and explanation; do not give the direct answer."},
    {"role": "user", "content": "This is the note from my class: "+ userMessage + "using this knowledge, answer my question: " + userQuestion}
  ]
)
  return completion.choices[0].message.content