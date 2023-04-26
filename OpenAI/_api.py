import os
import openai
import json

class Create:
    def __init__(self, key, prompt: str):
        openai.api_key = key
        self.response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Give me a short creative reply up to 120 characters for the following\n\n"+prompt,
            temperature=0.5,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )


    def getResponse(self):
        return self.response["choices"][0]["text"]
