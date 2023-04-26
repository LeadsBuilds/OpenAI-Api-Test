import Reader
import OscHandler
import OpenAI
import os
from dotenv import load_dotenv
import keyboard

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

reader = Reader.Create(1300, 535, 800, 300)

def sendResponse():
    print ("\n\nGenerating based on screen text...")
    osc = OscHandler.Create();
    prompt = reader.read_screen()
    print(prompt);

    gpt = OpenAI.Create(key, prompt)
    response = gpt.getResponse()

    print(response)

    osc.sendMessage(response)

print ("Running...\n")
print ("Press CTRL + SHIT + 9 to generate a new GPT message")
print ("Press CTRL + SHIFT + 0 to exit")

keyboard.add_hotkey('ctrl+shift+9', sendResponse)
keyboard.wait('ctrl+shift+0')