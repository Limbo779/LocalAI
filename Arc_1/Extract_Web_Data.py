import os
import requests

# Set your Ollama API key either here or as an environment variable OLLAMA_API_KEY
API_KEY = os.getenv("OLLAMA_API_KEY", "13b1bb3fd0894359ba9c9da94aabbe76.LVr9Am3AtXNK4wNOCcybD-B0")

# Base URL for Ollama's web search API
WEB_SEARCH_URL = "https://ollama.com/api/web_search"

# Function to perform a web search with Ollama
def ollama_web_search(query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": query,
        "options": {
            "web_search": True  # This flag tells Ollama model to use web search
        }
    }
    
    response = requests.post(WEB_SEARCH_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed: {response.status_code} {response.text}")


def write_cleaned_content_to_md(data: dict, filename: str = "output.md"):
    """
    Extracts relevant fields from the given dict and writes them into a Markdown file.
    
    Args:
        data (dict): Dictionary containing 'title', 'url', and 'content' keys.
        filename (str): Name of the Markdown file to write.
    """
    title = data.get("title", "No Title")
    url = data.get("url", "No URL")
    content = data.get("content", "No Content")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**URL:** [{url}]({url})\n\n")
        f.write(f"{content}\n")

# Example use:
# my_dict = { ... }  # your dictionary as provided
# write_cleaned_content_to_md(my_dict, "mecha_anime.md")



if __name__ == "__main__":
    user_query = "what are the best pokemon games?"
    results = ollama_web_search(user_query)
    print("Web Search Results:")
    print(results['results'][2])
    write_cleaned_content_to_md(results['results'][0],'output.md')
    #for result in results.get("results", []):
    #    print(f"- Title: {result.get('title')}")
    #    print(f"  URL: {result.get('url')}")
    #    print(f"  Snippet: {result.get('content')}\n")
