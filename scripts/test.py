import os
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a music composer, very talented and progressive rock inspired."},
    {"role": "user", "content": "Compose a song talking about joy of life using Pink Floyd as inspiration."}
  ]
)

print(completion.choices[0].message)
