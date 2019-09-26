import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_json('dataDigi.json')
# print(df.head())
df = df[['digimon','stage','type','attribute']]
# print(df.head())

def kombinasi(i):
    return str(i['stage']) + ' ' + str(i['type']) +  ' ' + str(i['attribute'])
df['recom'] = df.apply(kombinasi, axis=1)
# print(df.head())

model = CountVectorizer(
    tokenizer = lambda i : i.split(' ')
)
hasil = model.fit_transform(df['recom'])
# print(model.get_feature_names())
cosskor = cosine_similarity(hasil)
# print(cosskor)

suka = 'Kudamon'
indexsuka = df[df['digimon']== suka].index.values[0]
# print(indexsuka)

digi = list(enumerate(cosskor[indexsuka]))
sortdigi = sorted(digi, key= lambda x : x[1], reverse=True)
# print(sortdigi)

for i in sortdigi[:5]:
    if df.iloc[i[0]]['digimon'] != suka:
        nama = df.iloc[i[0]]['digimon']
        stage = df.iloc[i[0]]['stage']
        tipe = df.iloc[i[0]]['type']
        attribute = df.iloc[i[0]]['attribute']
        print(f'{i[0]}, {nama}, {stage}, {type}, {attribute} {round(i[1]*100)}%')

# # CREATE MODEL
import pickle
with open('model.pkl','wb') as mymodel:
          pickle.dump(cosskor,mymodel)


