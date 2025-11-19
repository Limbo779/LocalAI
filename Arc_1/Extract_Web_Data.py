import os
import requests
import re
import subprocess

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

#function to remove the annoying links in the md
def remove_links_from_md(md_text):
    pattern = r"\[(.*?)\]\(.*?\)"
    cleaned_text = re.sub(pattern, r"\1", md_text)
    return cleaned_text

def convert_md_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = remove_links_from_md(content)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

# Example usage:
# convert_md_file('input.md', 'output_cleaned.md')


# this will pull take the three web data, remove all the annoying link and write them into three md files
if __name__ == "__main__":
    user_query = "why few people use linux"
    results = ollama_web_search(user_query)
    #print("Web Search Results:")
    j=0
    for i in ['output1.md','output2.md','output3.md'] :
        #print(results['results'][2])
        write_cleaned_content_to_md(results['results'][j],i)
        j+=1
        convert_md_file(i,f"output_{j}.md")
        subprocess.run(f'rm -rf {i}',shell=True)
    print("Data Extraction Completed")
    subprocess.run(f'python3 test.py',shell=True)

    #for result in results.get("results", []):
    #    print(f"- Title: {result.get('title')}")
    #    print(f"  URL: {result.get('url')}")
    #    print(f"  Snippet: {result.get('content')}\n")
