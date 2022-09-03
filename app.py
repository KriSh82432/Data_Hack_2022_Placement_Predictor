from unicodedata import name
from flask import Flask,request, url_for, redirect, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/form.html',methods=['POST','GET'])
def predict():
    return render_template("form.html")
    '''features = [int(x) for x in request.form.values()]
    value = [np.array(features)]
    print(features)
    print(value)'''
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
