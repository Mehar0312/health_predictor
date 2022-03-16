# from crypt import methods
# from urllib import response
from flask import Flask, render_template, request
# import requests
import pickle
# from bs4 import BeautifulSoup
import numpy as np


app = Flask(__name__)
model_cancer = pickle.load(open("cancer_model.pkl", 'rb'))
model_diabetes = pickle.load(open("diabetes_model.pkl", 'rb'))
model_heart = pickle.load(open("heart_model.pkl", 'rb'))
model_kidney = pickle.load(open("kidney_model.pkl", 'rb'))
model_liver = pickle.load(open("liver_model.pkl", 'rb'))


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cancer', methods = ['GET', 'POST'])
def cancer():
  return render_template('cancer.html')

@app.route('/cancer_predict', methods = ['POST'])

def cancer_predict():

  data1 = request.form['a']
  data2 = request.form['b']
  data3 = request.form['c']
  data4 = request.form['d']
  data5 = request.form['e']
  data6 = request.form['f']
  data7 = request.form['g']
  data8 = request.form['h']
  data9 = request.form['i']
  data10 = request.form['j']

 
  arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]])
  pred = model_cancer.predict(arr)
  return render_template("after.html", data = pred)

@app.route('/diabetes', methods = ['GET', 'POST'])
def diabetes():
  return render_template('diabetes.html')

@app.route('/diabetes_predict', methods = ['POST'])

def diabetes_predict():

  data1 = request.form['a']
  data2 = request.form['b']
  data3 = request.form['c']
  data4 = request.form['d']
  data5 = request.form['e']
  data6 = request.form['f']
  
 
  arr = np.array([[data1,data2,data3,data4,data5,data6]])
  pred = model_diabetes.predict(arr)
  return render_template("after.html", data = pred)


@app.route('/liver', methods = ['GET', 'POST'])
def liver():
  return render_template('liver.html')

@app.route('/liver_predict', methods = ['POST'])

def liver_predict():

  data1 = request.form['a']
  data2 = request.form['b']
  data3 = request.form['c']
  data4 = request.form['d']
  data5 = request.form['e']
  data6 = request.form['f']
  data7 = request.form['g']
  data8 = request.form['h']
  data9 = request.form['i']
  data10 = request.form['j']
  
  
 
  arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]])
  pred = model_liver.predict(arr)
  return render_template("after.html", data = pred)


@app.route('/heart', methods = ['GET', 'POST'])
def heart():
  return render_template('heart.html')


@app.route('/heart_predict', methods = ['POST'])

def heart_predict():

  data1 = request.form['a']
  data2 = request.form['b']
  data3 = request.form['c']
  data4 = request.form['d']
  data5 = request.form['e']
  data6 = request.form['f']
  data7 = request.form['g']
 
  arr = np.array([[data1,data2,data3,data4,data5,data6,data7]])
  pred = model_heart.predict(arr)
  return render_template("after.html", data = pred)


@app.route('/kidney', methods = ['GET', 'POST'])
def kidney():
  return render_template('kidney.html')


@app.route('/kidney_predict', methods = ['POST'])

def kidney_predict():

  data1 = request.form['a']
  data2 = request.form['b']
  data3 = request.form['c']
  data4 = request.form['d']
  data5 = request.form['e']
  data6 = request.form['f']
  data7 = request.form['g']
  data8 = request.form['h']

  arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8]])
  pred = model_kidney.predict(arr)
  return render_template("after.html", data = pred)




if __name__ == '__main__':
  app.run(debug = True)