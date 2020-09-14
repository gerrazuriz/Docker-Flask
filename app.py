from flask import Flask,send_file,render_template
import os
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
fig2,ax=plt.subplots(figsize=(6,3))
ax = sns.set(style="darkgrid")
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
@app.route('/')
def home():
 return render_template('index.html')
@app.route('/visualize3')
def visualize3():
 df = pd.read_csv("default_credit.csv")
 sns.distplot(df["income"]*np.random.random_sample() + 100000*np.random.random_sample())
 canvas=FigureCanvas(fig2)
 img2 = io.BytesIO()
 fig2.savefig(img2)
 img2.seek(0)
 return send_file(img2,mimetype='img/png', cache_timeout=0)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)