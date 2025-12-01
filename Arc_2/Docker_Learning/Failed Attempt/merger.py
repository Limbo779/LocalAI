import os
import sys
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer, util

def read_md_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def split_sentences(content):
    return sent_tokenize(content)

def semantic_sort_and_mix(sentences1, sentences2):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    emb1 = model.encode(sentences1, convert_to_tensor=True)
    emb2 = model.encode(sentences2, convert_to_tensor=True)

    # Create pairs based on maximum similarity
    used1 = set()
    used2 = set()
    mixed = []
    for i, e1 in enumerate(emb1):
        sims = util.pytorch_cos_sim(e1, emb2)[0]
        idx = sims.argmax().item()
        if idx not in used2:
            mixed.append((sentences1[i], sentences2[idx]))
            used1.add(i)
            used2.add(idx)
    # Add remaining sentences
    for i, s in enumerate(sentences1):
        if i not in used1:
            mixed.append((s, None))
    for i, s in enumerate(sentences2):
        if i not in used2:
            mixed.append((None, s))

    # Flatten and remove Nones
    final = []
    for tup in mixed:
        for s in tup:
            if s:
                final.append(s)
    return final

def main(md_file1, md_file2, out_file):
    content1 = read_md_file(md_file1)
    content2 = read_md_file(md_file2)

    sentences1 = split_sentences(content1)
    sentences2 = split_sentences(content2)

    mixed_sentences = semantic_sort_and_mix(sentences1, sentences2)

    # Optionally, summarize if too long
    parser = PlaintextParser.from_string("\n".join(mixed_sentences), Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, min(30, len(mixed_sentences)))
    summary_text = "\n".join(str(sent) for sent in summary)

    # Save
    with open(out_file, "w", encoding="utf-8") as fout:
        fout.write(summary_text)

if __name__ == "__main__":
    #if len(sys.argv) != 4:
    #    print("Usage: python combine_md_files.py <file1.md> <file2.md> <output.md>")
    #    sys.exit(1)
    md_file1 = input() #sys.argv[1]
    md_file2 = input() #sys.argv[2]
    out_file = input() #sys.argv[3]
    main(md_file1, md_file2, out_file)