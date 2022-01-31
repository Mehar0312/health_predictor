# from crypt import methods
from flask import Flask, render_template

app = Flask(__name__)

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