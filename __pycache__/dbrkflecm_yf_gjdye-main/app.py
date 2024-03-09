
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__, template_folder='', static_folder='')
from db import get_all_products



app = Flask(__name__, template_folder='', static_folder='')



@app.route("/")
def index():
    return render_template('home.html', products=get_all_products())


@app.route("/home/<id>")
def home(id):
    
    for products in data:
        if products['id'] == id:
            return render_template('products.html', showed_news=news, ids=news_id)

    
    return redirect('/')



app.run(debug=True)
