from flask import Flask, render_template, request
#from models import *

app = Flask(__name__)


@app.route("/")
def index():
    return {"message": "hello"}
    #return "hello"
    #return render_template('index.html', message="Test")

if __name__ == "__main__":
    app.run()
