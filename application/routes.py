

# decorating index function with the app.route
from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")