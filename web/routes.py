from web import app
from flask import  request, render_template
import os


@app.route("/search",methods=["POST","GET"])
def search():
    if request.method == "POST":
        todo = request.form.get("todo")
        print(todo)
        return render_template('data.html')
    # return render_template('index.html',data="null")
@app.route("/",methods=["POST","GET"])
def home():
    return render_template('index.html',data="null")