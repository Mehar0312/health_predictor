# from crypt import methods
# from urllib import response
from flask import Flask, render_template, jsonify, request
# import requests
# import pickle
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd


app = Flask(__name__)

# def findinfo(cname):
#   totalresult = []
#   country = cname
#   url = "https://www.worldometers.info/coronavirus/country/{countryname}/".format(country)
#   response = requests.get(url)
#   if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     result = soup.find_all('div', class_="maincounter-number")
#     for i in result:
#       totalresult.append(i.find("span".text))
#   else:
#     totalresult.append("No Result")
#   return totalresult  

# @app.route("/info/", methods = ['GET'])
# def findinformation():
#   country = request.get("country")
#   try:
#     return jsonify({"Total Cases: ": findinfo(country)[0], "Total Deaths: ": findinfo(country)[1], "Total Recovered: ": findinfo(country)[2]})
#   except:
#     return jsonify({"No country found!!"})


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cancer', methods = ['GET', 'POST'])
def cancer():
  return render_template('cancer.html')

@app.route('/diabetes', methods = ['GET', 'POST'])
def diabetes():
  return render_template('diabetes.html')

@app.route('/liver', methods = ['GET', 'POST'])
def liver():
  return render_template('liver.html')

@app.route('/heart', methods = ['GET', 'POST'])
def heart():
  return render_template('heart.html')

@app.route('/kidney', methods = ['GET', 'POST'])
def kidney():
  return render_template('kidney.html')

if __name__ == '__main__':
  app.run(debug = True)