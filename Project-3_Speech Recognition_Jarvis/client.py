from openai import OpenAI

client = OpenAI(
    api_keys = "Enter Your API keys"
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages = [
        {"role": "system", "content" : "You are a virtual assistant Named jarvis skilled in general task like Google and Alexa"},
        {"role": "user", "content": "what is coding?"}
    ]
)

print(completion.choices[0].message.content)
