# Currently testing the summarizer
from ollama import Client

# Create a client pointing to your local Ollama server (default URL)
client = Client(host="http://localhost:11434")

def read_md_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

raw_info=read_md_file('output.md')

# Chat with your local model by specifying the model name and messages
response = client.chat(
    model="llama3.1:8b",
    messages=[
        {"role": "user", "content": f"summarize and get the key points from the following text for llm model to understand     text : {raw_info}"}
    ]
)

# Print the model's response content
print(response["message"]["content"])
