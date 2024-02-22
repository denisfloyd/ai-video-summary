import os
import sys
import openai
import pysrt

client = OpenAI()
input_data = sys.stdin.read()

prompt_base = (
    "You are going to be a good text summarizer. "
    "Take the following text and create a summary of it, "
    "with two hundreds words maximum. "
    "Summarize from [START] to [END]:\n[START]\n"
)


def summarizer_text(text):
    prompt = prompt_base
    prompt += text + "\n[END]"

    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        temperature=0,
    )
    summary = response.choices[0].text.strip()
    return summary

summary_text = summarizer_text(input_data)
print(summary_text, flush=True)
