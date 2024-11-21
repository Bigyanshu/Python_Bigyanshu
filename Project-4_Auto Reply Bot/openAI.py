# # Create the chat completion
# completion = client.chat.completions.create(
# model="gpt-3.5-turbo",
# messages =
# [
#     {"role": "system", "content" : "You are a person named Mahi, who speaks Hindi as well as English. You are from India, and you are a coder. You analyze chat history and response (test message only)"},# like Mahi.\n\n{command}"},
    
#     {"role" : "user", "content" : chat_history}
# ]
# )

import openai

# Set your API key here
openai.api_key = "Enter API keys"

# Command text for the prompt
command = '''
[12:19 AM, 11/7/2024] OMM: add hba
[12:19 AM, 11/7/2024] OMM: sethire add karithily
[12:19 AM, 11/7/2024] Mahy: To voice commands re chalichi I think
[12:20 AM, 11/7/2024] OMM: so chenz kari ethire kariby
[12:20 AM, 11/7/2024] OMM: normal typing
[12:20 AM, 11/7/2024] Mahy: Mu group re msg karibi?
[12:20 AM, 11/7/2024] OMM: no voice command
[12:20 AM, 11/7/2024] OMM: ebe nuha
[12:20 AM, 11/7/2024] OMM: pare
[12:20 AM, 11/7/2024] Mahy: Kali
[12:20 AM, 11/7/2024] Mahy: Ok
[12:20 AM, 11/7/2024] OMM: ok soipad
[12:20 AM, 11/7/2024] OMM: sarila
[12:20 AM, 11/7/2024] OMM: mo bot ready hba
[12:20 AM, 11/7/2024] Mahy: Tu bi so
[12:20 AM, 11/7/2024] OMM: enough etiki re msg
[12:20 AM, 11/7/2024] Mahy: No mobile or no msg
'''

# Create the chat completion using the updated API method
completion = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=f"You are a person named Mahi, who speaks Hindi as well as English. You are from India, and you are a coder. You analyze chat history and respond like Mahi.\n\n{command}",
    max_tokens=150
)

# Extract and print the response
response = completion.choices[0].text.strip()
print("AI Response:", response)
