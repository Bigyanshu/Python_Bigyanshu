import pyautogui

while True:
    a = pyautogui.position()
    print(a)

''' & then drag from 10455, 325 to 1186, 1552
select a text & then copy it to clipboard 
then take it in variable

import pyautogui
import pyperclip
import time
from openai import OpenAI

import os
import openai

# client = openai.ChatCompletion(
#     api_key=os.getenv("OPENAI_API_KEY")  # Retrieves API key from environment
# )


client = OpenAI(
    api_key = " " # Enter your API key
)
def is_last_message_from_sender(chat_log, sender_name = "Mahy"):

    # Split the chat log into individual messages
    message = chat_log.strip().split("/2024] ")[-1]
    if sender_name in message:
        return True
    return False
       
 # Step 1: Click on the icon at (1913, 1756)
pyautogui.click(1632, 1741)
time.sleep(1)  # Wait for 1 sec to ensure click is register

while True:

    # Step 2: Drag from (986, 241) to (2824, 1564) to select text
    pyautogui.moveTo(1028, 331)
    pyautogui.dragTo(1186,1552, duration=1, button = "left")  # Drag with a duration for smooth movement

    # Step 3: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait a bit for the clipboard to update
    pyautogui.click(1028, 331)

    # Step 4: Retrieve the text from the clipboard
    chat_history = pyperclip.paste()

    # Print Copied text to verify
    print("Copied Text:", chat_history)

    if is_last_message_from_sender(chat_history):

        completion = client.ChatCompletion.create( #client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages =
        [
            {"role": "system", "content" : "You are a person named Mahi, who speaks Hindi as well as English. You are from India, and you are a coder. You analyze chat history and response (test message only)"},# like Mahi.\n\n{command}"},
            
            {"role" : "user", "content" : chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at co-ordinate( , )
        pyautogui.click(1028, 331)
        time.sleep(1)

        # Step 6 : Paste text from
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 7: Press Enter
        pyautogui.press('enter')

        # print(completion.choice[0].message.content)

'''
