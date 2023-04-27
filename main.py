import Reader
import OscHandler
import OpenAI
import os
from dotenv import load_dotenv
import keyboard

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
ai_name = "Downluck"
reader = Reader.Create(1300, 535, 800, 300)

gpt = OpenAI.Create(key, ai_name)

def send_respose():
    print ("\n\nGenerating based on screen text...")
    osc = OscHandler.Create();
    prompt = reader.read_screen()
    gpt.generate_response(prompt)
    response = gpt.get_respose()

    print("\nPrompt: "+prompt)
    print(response)
    osc.send_message(response)

print ("Running...\n")
print ("Press CTRL + SHIFT + 9 to generate a new GPT message")
print ("Press CTRL + SHIFT + 0 to exit")

keyboard.add_hotkey('ctrl+shift+9', send_respose)
keyboard.wait('ctrl+shift+0')