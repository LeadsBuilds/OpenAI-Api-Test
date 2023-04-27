import openai

class Create:
    def __init__(self, key, ai_name: str):
        self.ai_name = ai_name
        self.prompt_id = 1
        self.prompt = "The following is a short conversation between a Human and "+ai_name+", you are "+ai_name+". "+ai_name+", is joyful, creative, clever, and very friendly. You should remember the conversation as you go and you should reply only using up to 100 characters\n"
        
        openai.api_key = key

    def generate_response(self, prompt: str):
        start_sequence = "\n" + self.ai_name + ": "
        restart_sequence = "\nHuman: "

        self.prompt =  self.prompt + restart_sequence + prompt + start_sequence
        if self.prompt_id > 1:
            self.prompt = restart_sequence + prompt + start_sequence

        self.response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt,
            temperature=0.9,
            max_tokens=30,
            top_p=1,
            frequency_penalty=0.6,
            presence_penalty=0.6,
            stop=[" Human:", " "+ self.ai_name + ":"]
        )

    def get_respose(self):
        self.prompt_id += 1
        return self.response["choices"][0]["text"]
