
from flask import Flask, render_template, redirect, url_for, request, session
app = Flask(__name__, template_folder='', static_folder='')
from db import get_all_news



app = Flask(__name__, template_folder='', static_folder='')



@app.route("/")
def index():
    print(get_all_news())
    return render_template('home.html', news=get_all_news())


@app.route("/home/<id>")
def home(id):
    
    for news in data:
        if news['id'] == id:
            return render_template('news.html', showed_news=news, ids=news_id)

    
    return redirect('/')
def profile():
    if 'user' in session.keys() and session['user']:
        add_pcoduct(request.form.get('title'), request.form.get('description'), request.form.get('image'), 1,1)
        return render_template('profile.html')
    else:
        return redirect(url_for('signIn'))


app.run(debug=True)
