#!pip install -U sentence-transformers
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer
import subprocess
model = SentenceTransformer('all-MiniLM-L6-v2')


def enc(s):
    return model.encode([s])[0]

def sim(s1,s2):
    return 1-distance.cosine(enc(s1),enc(s2))

querry = input()

with open('data.txt','r') as file:
    lines=file.readlines()

d={}

for i in lines:
    d[float(sim(querry,i))]=i

d = dict(sorted(d.items(),reverse=True))

subprocess.run('rm -rf data.txt',shell=True)

list_len=len(list(d.values()))
list_len = int(list_len*0.75)

with open('data.txt','a+',encoding='utf-8') as file:
    for sentance in list(d.values())[0:list_len] :
        file.write(str(sentance)+'\n')
       
#encoding : enc1 = model.encode([str])[0]
#getting similarity : 1-distance.cosine(enc1,enc2)
