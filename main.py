from flask import Flask, render_template, url_for, request, json, redirect

from loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['username'] = "Mars One"
    param['title'] = title
    return render_template('index.html', **param)

@app.route('/')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['username'] = "Mars One"
    param['title'] = title
    return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

@app.route('/news')
def news():
    with open('data/news.json', "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

@app.route('/vars')
def vars():
    return render_template('vars.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)
# lkdvd;lvv


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

