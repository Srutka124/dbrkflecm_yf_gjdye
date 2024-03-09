
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__, template_folder='', static_folder='')
from db import get_all_products,get_product_by_id



app = Flask(__name__, template_folder='', static_folder='')



@app.route("/")
def index():

    return render_template('home.html', products=get_all_products())


@app.route("/home/<id>")
def home(id):
    product = get_product_by_id(id)
    if product:
        return render_template('products.html', product=product[0])

    
    return redirect('/')
@app.route("/home/depe_admin")
def depe_admin():
    return render_template('depe_admin.html',)




app.run(debug=True)
