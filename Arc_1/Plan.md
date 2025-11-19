# Plan Right now :

## Trying to implement the entire pipeline locally in a simple way

# 18 Nov 2025

- Local AI can't summarize that big data so let's get a non AI summarizer 
- Let's look for some code in Github or get from perplexity
- Let's use sumy package as it is simple and easy to use 
- This is more than enough for getting the proper data for model
- i will use sumy to clean the data for AI and use model to determine the points needed for final generation 
- finally the key points will be used for making the final generation
- summary.py is the script that will do the magic which will take output md file and make data md file where summary points are stored
- choose_points.py will pick the most relevent point for the querry and store it in a txt file
- make a tool which will let ollama access txt file in python (tool.py) and use it so that model can access txt easily
- all this will be orchestrated in main.py which will call all these py files in required time 

# 19 Nov 2025

- Summarizer is ready.so each summary algo has it's own advantage so when spliting the querry into three let the AI decide what algo to use
- and based on that we can use that algo 
- when the querry is split into 3 different querry ,Extract_Web_Data.py will be used and summarization will be done based on the choice (Extract_Web_Data.py will run the summary.py)
- all the summarized data from 3 different querry will be written into one file data.txt
- choose_points.py will go through data.py and give the most relevent thing based on semantic simillarity 
- resources to consult for semantic simillarity [1](https://www.geeksforgeeks.org/nlp/different-techniques-for-sentence-semantic-similarity-in-nlp/) [2](https://www.freecodecamp.org/news/how-to-perform-sentence-similarity-check-using-sentence-transformers/) [3](https://huggingface.co/tasks/sentence-similarity)
- today's [perplexity chat](https://www.perplexity.ai/search/localai-tell-me-how-to-build-a-F4lQoKvqQVqJQwGduao6oA#0)
- tommorrow let's analyse what semantic simillarity is and how we can apply in our project