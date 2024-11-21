import pyautogui
import pyperclip
import time
import openai  # Import the openai module directly
import os

# Set your API key here
openai.api_key = "Enter Your API keys"  # Replace with your actual API key or use environment variable

# Set API key from environment variable
# openai.api_key = os.getenv("3ec7bd69fbfe41f7a0d5a1ab37343b08")  # Ensure the environment variable is set correctly
# Set API key in ur system environment then work properly with environment variable

def is_last_message_from_sender(chat_log, sender_name="Mahy"):
    # Split the chat log into individual messages
    message = chat_log.strip().split("/2024] ")[-1]
    if sender_name in message:
        return True
    return False

# Step 1: Click on the icon at (1913, 1756)
pyautogui.click(1552, 1743)
time.sleep(1)  # Wait for 1 sec to ensure click is registered

while True:
    # Step 2: Drag from (986, 241) to (2824, 1564) to select text
    pyautogui.moveTo(1028, 331)
    pyautogui.dragTo(1186, 1552, duration=1, button="left")  # Drag with a duration for smooth movement

    # Step 3: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait a bit for the clipboard to update
    pyautogui.click(1028, 331)

    # Step 4: Retrieve the text from the clipboard
    chat_history = pyperclip.paste()

    # Print copied text to verify
    print("Copied Text:", chat_history)

    if is_last_message_from_sender(chat_history):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Mahi, who speaks Hindi as well as English. You are from India, and you are a coder. You analyze chat history and respond (test message only)"},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message['content']
        pyperclip.copy(response)

        # Step 5: Click at coordinate (1028, 331)
        pyautogui.click(1028, 331)
        time.sleep(1)

        # Step 6: Paste text from clipboard
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 7: Press Enter
        pyautogui.press('enter')
