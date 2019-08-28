# @file app.py
#
# @ref https://github.com/ecerami/hello_flask/blob/master/app.py
# @ref https://github.com/ericmjl/minimal-flask-example/blob/master/app.py

from flask import Flask, render_template

import pandas as pd
import numpy as np

df = pd.read_csv("data/FRB_G19.csv")

length = len(df)

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
# def home():
  # Read in the Data via Pandas
  fruit_df = pd.read_table("data/fruit.txt")
  return render_template("index.html.j2")

#@app.route("/df")
#def dataframe():
#  return render_template("df.html.j2", length=length, dataframe=df.to_html())


if __name__ == '__main__':
  #app.run(debug=True, port=5957)
  app.run(debug=True)
