from unicodedata import name
from flask import Flask,request, url_for, redirect, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/form.html',methods=['POST','GET'])
def form():
    return render_template("form.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    features = [x for x in request.form.values()]
    #value = [np.array(features)]
    print(features)
    for x in features:
        print(x)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
