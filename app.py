
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__, template_folder='', static_folder='')
from db import get_all_products,get_product_by_id,add_products,drop_tabel,get_all_progect
import sqlite3
conn = None
cursor= None



app = Flask(__name__, template_folder='', static_folder='')



@app.route("/")
def index():

    return render_template('home.html', products=get_all_products())


@app.route("/home/pass")
def pasport():

    return render_template('pass.html', progect=get_all_progect())







@app.route("/home/<id>")
def home(id):
    product = get_product_by_id(id)
    if product:
        return render_template('products.html', product=product[0])

    
    return redirect('/')
@app.route("/home/depe_admin")
def depe_admin():
    return render_template('depe_admin.html',)

@app.route("/profile")
def profile():
    return render_template('plus.html')

@app.route("/plus", methods=['POST'])
def plus():
    if request.method == 'POST':
        a = request.form.get('name')
        c = request.form.get('infa')
        b = request.form.get('img')
        d = request.form.get('price')
        i = request.form.get('status')
        f = request.form.get('point')

        add_products(i,f,c,b,d,a)
    if request.form.get('delit') == 'POST':
        drop_tabel()
    
    return redirect(url_for('profile'))


@app.route("/home/login" , methods=["GET","POST"])
def login():
    
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['user'] = True
            session['inccorect_pass'] = False
            return redirect('/profile')
        else:
            session['inccorect_pass'] = True
            return redirect(url_for('login'))
            
    if ('inccorect_pass' in session.keys()  ):
        return render_template('login.html', incorrect_password=session['inccorect_pass'])
    
    return render_template('login.html', incorrect_password=False)


app.secret_key = 'wewewe32-0fdfrkrrf'
app.run(debug=True)
