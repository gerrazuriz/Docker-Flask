from flask import Flask, send_file, render_template, request
import os
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from joblib import load

#fig2,ax=plt.subplots(figsize=(6,3))
#ax = sns.set(style="darkgrid")
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
genre_model = load("genre_model")
genre_list = ["Hip Hop", "Metal", "Pop", "Rock"]
lyrics = 'give me baby one more time'

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/predict')
def predict():
    fig2,ax=plt.subplots(figsize=(8,4))
    #lyrics = request.args.get('lyrics', 'Give me baby one more time')
    #ax = sns.set(style="darkgrid")
    prob = genre_model.predict_proba([lyrics])

    df_prediction = pd.concat([pd.DataFrame(genre_list, columns = ["Genre"]),
                           pd.DataFrame(prob[0], columns = ["Probability"])], axis = 1)
    
    sns.barplot(x = df_prediction.Genre, y = df_prediction.Probability)
    
    canvas=FigureCanvas(fig2)
    img2 = io.BytesIO()
    fig2.savefig(img2)
    img2.seek(0)
    return send_file(img2,mimetype='img/png', cache_timeout=0);

#@app.route('/predict2')
#def predict2():
#    global lyrics = request.args.get('lyrics')

@app.route("/prediction/")
def predict2():
    global lyrics
    lyrics = request.args.get('lyrics', 'Give me baby one more time')

    most_likely_genre = genre_model.predict([lyrics])[0]

    if most_likely_genre == "hiphop":
        most_likely_genre = "Hip Hop"
    else:
        most_likely_genre = most_likely_genre.capitalize()

    genre_proba = str(int(genre_model.predict_proba([lyrics])[0].max() * 100)) + "%"

    return render_template('prediction.html',
        genre_proba = genre_proba,
        most_likely_genre = most_likely_genre);

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)