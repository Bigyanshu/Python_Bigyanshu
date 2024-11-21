from openai import OpenAI

client = OpenAI(
    api_keys = "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"
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages = [
        {"role": "system", "content" : "You are a virtual assistant Named jarvis skilled in general task like Google and Alexa"},
        {"role": "user", "content": "what is coding?"}
    ]
)

print(completion.choices[0].message.content)