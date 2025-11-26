from ollama import chat
import subprocess
import json
import os
import ollama

def split_query(s):
    messages = [
      {
        'role':'system',
        'content':"""You are an expert query analyzer and optimization engine. Your goal is to decompose complex user requests into three distinct, targeted search queries to gather comprehensive data from the web.

For each of the three queries you generate, you must also select the single most appropriate summarization algorithm from the 'sumy' package based on the nature of the information being sought. Use the following logic for algorithm selection:

- "Luhn": Use this for factual queries requiring extraction of specific dates, names, locations, or hard data (e.g., stock prices, birth dates, specific events).
- "LSA": Use this for general concepts, broad topics, or when understanding the underlying context/theme is more important than specific facts (e.g., "history of internet", "concepts of quantum physics").
- "LexRank": Use this for structured texts, conversational data, or when identifying the most "central" or "important" sentences in a narrative is key (e.g., "podcast transcripts", "interviews", "forum discussions").
- "Edmundson": Use this ONLY if the query is highly domain-specific and would benefit from custom keyword weighting (e.g., "medical research papers", "legal documents"). If unsure, prefer LSA or Luhn.

You must return your response strictly as a valid JSON object. Do not include any conversational text, markdown formatting, or explanations outside the JSON. The JSON structure must be exactly as follows:

{
  "queries": [
    {
      "query": "The first specific search query",
      "algorithm": "Name of the algorithm (Luhn, LSA, LexRank, or Edmundson)",
      "reasoning": "Brief reason for choosing this algorithm"
    },
    {
      "query": "The second specific search query",
      "algorithm": "Name of the algorithm",
      "reasoning": "Brief reason for choosing this algorithm"
    },
    {
      "query": "The third specific search query",
      "algorithm": "Name of the algorithm",
      "reasoning": "Brief reason for choosing this algorithm"
    }
  ]
}
"""
      },
      {
        'role': 'user',
        'content': str(s),
      }
    ]

    response = chat('gemma3:4b', messages=messages)
    return (response['message']['content'])


# splitting the query and storing it in queries dict
query = input('Enter the querry : ')
print()
print("Prompt preprocessing.....\n")
queries = ((str(split_query(query))).replace('json','')).replace('`','')

queries = json.loads(queries)
print("Done\n")

print("extracting the web data .....\n")

for i in range(3):
    q = queries['queries'][i]['query']
    a = queries['queries'][i]['algorithm']

    d = json.dumps({'q':q,'a':a})
    
    subprocess.run(
            ['python3', 'Extract_Web_Data.py'], 
            input=d.encode('utf-8'),
            check=True  # Optional: raises an error if the script fails
        )
print("Done\n")
# choosing and organizing points from data.txt
subprocess.run(
        ['python3', 'choose_points.py'], 
        input=query.encode('utf-8'),
        check=True  # Optional: raises an error if the script fails
    )

# the final response part

# 1. Define the tool (function)
def read_local_file(filepath: str) -> str:
    """
    Reads data from a local text file.
    
    Args:
        filepath: The path to the file to read (e.g., 'data.txt').
        
    Returns:
        The content of the file as a string, or an error message if not found.
    """
    if not os.path.exists(filepath):
        return f"Error: The file '{filepath}' does not exist."
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

# 2. Set up the chat history
# We give the model instructions to use the tool when needed.
messages = [
    {'role': 'user', 'content': f'{query}. you may use the "data.txt" file which will have recent info you may need'}
]

print("Thinking...")

# 3. First API Call: Send query + available tools
response = ollama.chat(
    model='llama3.1:8b',
    messages=messages,
    tools=[read_local_file] # Pass the actual function here
)

# 4. Check if the model decided to use the tool
if response.message.tool_calls:
    # The model wants to use a tool. Let's verify which one and execute it.
    for tool in response.message.tool_calls:
        
        # Check if the function requested is the one we defined
        if tool.function.name == 'read_local_file':
            filepath = tool.function.arguments['filepath']
            print(f"Model requested to read: {filepath}")
            
            # Execute the actual Python function
            file_content = read_local_file(filepath)
            
            # Add the tool's output to the conversation history
            messages.append(response.message) # Append the model's tool request
            messages.append({
                'role': 'tool',
                'content': file_content,
            })

    # 5. Second API Call: Get the final answer
    # The model now has the file content in the history and can answer the question.
    final_response = ollama.chat(model='llama3.1:8b', messages=messages)
    print("\nFinal Answer:")
    print(final_response.message.content)
    subprocess.run('rm data.txt',shell=True)

else:
    # The model didn't need the tool (e.g., if you asked "What is 2+2?")
    print(response.message.content)
    subprocess.run('rm data.txt',shell=True)
