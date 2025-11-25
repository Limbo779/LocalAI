#!pip install -U sentence-transformers

# importing all these bloody modules will take more time than actual code running
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer
import subprocess
model = SentenceTransformer('all-MiniLM-L6-v2')

# encode text into vector embedding
def enc(s):
    return model.encode([s])[0]

# find the simillarity between two sentance
def sim(s1,s2):
    return 1-distance.cosine(enc(s1),enc(s2))

# the querry is recieved through pipe from main.py
querry = input()

with open('data.txt','r') as file:
    lines=file.readlines()

d={}

for i in lines:
    d[float(sim(querry,i))]=i # each lines has their simillarity factor with querry

d = dict(sorted(d.items(),reverse=True)) # most simillar lines are sorted at top

subprocess.run('rm -rf data.txt',shell=True)

list_len=len(list(d.values()))
list_len = int(list_len*0.20) # only 20 % of the top lines will be finalised

# finally all the top 50 % lines are written into data.txt 
with open('data.txt','a+',encoding='utf-8') as file:
    for sentance in list(d.values())[0:list_len] :
        file.write(str(sentance)+'\n')
       
#encoding : enc1 = model.encode([str])[0]
#getting similarity : 1-distance.cosine(enc1,enc2)
