import openai

openai.api_key = "your-api-key-here"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if available
    messages=[
        {"role": "user", "content": "Tell me a short AI story."}
    ]
)

print(response.choices[0]['message']['content'])