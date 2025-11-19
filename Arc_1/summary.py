import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.kl import KLSummarizer

def summarize(text, language="english"):
    # Get the token count
    count=len(nltk.word_tokenize(text))
    # Parse text and tokenize
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    # Choose summarizer
    summarizer = LexRankSummarizer() #LsaSummarizer()
    # Generate summary as a list of sentences
    sentences_count=int(round(count*(1/100)))
    summary = summarizer(parser.document, sentences_count)
    # Combine into one string to return
    
    return summary
    #return ' '.join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    text=""
    for i in range(3): # this loop is to summarize three md files
        # open the md file and summarize it
        with open(f"output_{i+1}.md",'r',encoding='utf-8') as f:
            text = f.read()
            text=summarize(text)

            # write the summarized text into data.txt line by line
            with open('data.txt','a+',encoding='utf-8') as file:
                for sentance in text :
                    file.write(str(sentance)+'\n')
    

