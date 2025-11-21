#!pip install -U sentence-transformers

from scipy.spatial import distance
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentence
sentences = ["i love cats" ,
             "We are learning NLP throughg GeeksforGeeks",
             "The baby learned to walk in the 5th month itself"]


test = "i love pets"
print('Test sentence:',test)
test_vec = model.encode([test])[0]


for sent in sentences:
    similarity_score = 1-distance.cosine(test_vec, model.encode([sent])[0])
    print(f'\nFor {sent}\nSimilarity Score = {similarity_score} ')


# encoding : enc1 = model.encode([str])[0]
# getting similarity : 1-distance.cosine(enc1,enc2)
