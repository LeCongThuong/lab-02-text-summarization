import os
import openai
from dotenv import load_dotenv
load_dotenv()


class OpenAISummarazation:
  def __init__(self):
    api_key = os.getenv('OPENAI_KEY')
    openai.api_key = api_key
    self.model_id = 'gpt-3.5-turbo'

  def summarize(self, content):
    response = openai.ChatCompletion.create(
      model=self.model_id,
      messages=[{"role": "user", "content": f"Tóm tắt nội dung văn bản sau bằng tiếng việt: {content}"}]
    )
    return response['choices'][0]['message']['content']
