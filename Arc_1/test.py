from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize(text, language="english", sentences_count=4):
    # Parse text and tokenize
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    # Choose summarizer
    summarizer = LsaSummarizer()
    # Generate summary as a list of sentences
    summary = summarizer(parser.document, sentences_count)
    # Combine into one string to return
    return ' '.join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    with open("output_1.md",'r',encoding='utf-8') as f:
        text=f.read()
    print(summarize(text))
