from flask import Flask, abort, jsonify, render_template,url_for, request,send_from_directory,redirect
import numpy as np 
import pandas as pd 
import json
import requests 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

data=pd.read_json('dataDigi.json')
def kombinasi(i):
    return str(i['stage'])+ ' ' +str(i['type'])+' '+str(i['attribute'])
data['recom']=data.apply(kombinasi,axis=1)
data['digimon']=data['digimon'].apply(lambda i: i.lower())

model = CountVectorizer(tokenizer=lambda data: data.split(' '))
hasil = model.fit_transform(data['recom'])
cosskor = cosine_similarity(hasil)


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['GET','POST'])
def Cari():
    body=request.form
    digi = body['digimon']
    digimon = digi.lower()
    if digimon not in list(data['digimon']):
        return redirect('/notfound')
    indexsuka = data[data['digimon'] == digimon].index.values[0]
    suka = data.iloc[indexsuka][['digimon','stage','type','attribute','image']]
    DigiScore = list(enumerate(skorDigi[indexsuka]))
    sortDigi = sorted(DigiScore,key=lambda i:i[1],reverse=True)
    recom=[]
    for item in sortDigi[:7]:
        x={}
        if data.iloc[item[0]]['digimon'] !=digimon:
            nama = data.iloc[item[0]]['digimon'].capitalize()
            stage = data.iloc[item[0]]['stage']
            gambar = data.iloc[item[0]]['image']
            tipe = data.iloc[item[0]]['type']
            attribute=data.iloc[item[0]]['attribute']
            x['digimon']=nama
            x['stage']=stage
            x['image']=gambar
            x['type']=Type
            x['attribute']=attribute
            recom.append(x)
    return render_template('hasil.html',rekomen=recom,suka = suka ) 


@app.route('/notfound')
def notFound():
    return render_template('notfound.html')


if __name__=='__main__':
    app.run(debug=True)