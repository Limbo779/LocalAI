from ollama import chat
import subprocess
import json

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
queries = ((str(split_query(query))).replace('json','')).replace('`','')

queries = json.loads(queries)

# extracting the web data

for i in range(3):
    q = queries['queries'][i]['query']
    a = queries['queries'][i]['algorithm']

    d = json.dumps({'q':q,'a':a})
    
    subprocess.run(
            ['python3', 'Extract_Web_Data.py'], 
            input=d.encode('utf-8'),
            check=True  # Optional: raises an error if the script fails
        )

# choosing and organizing points from data.txt
subprocess.run('python3 choose_points.py',shell=True)
print('done')