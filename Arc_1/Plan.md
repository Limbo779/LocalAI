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