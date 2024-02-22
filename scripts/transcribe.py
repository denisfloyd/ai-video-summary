import os
import openai
import sys
client = OpenAI()
video_id = sys.argv[1]
audio_file_path = os.path.join(os.getcwd(), 'tmp', video_id + '.m4a')

prompt_file_path = os.path.join(os.getcwd(), 'tmp', 'prompt.txt')
f = open(prompt_file_path, "r")
prompt = f.read()

audio_file = open(audio_file_path, 'rb')
transcript = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
    response_format="text",
    prompt=prompt
)
print(transcript)
