from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm
from .models import User

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'Jerry'},
            'body': 'Beautiful day in Boston!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool.'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(nickname=request.form['nickname']).first()
        if user and request.form['password'] == user.password:
            session['logged_in'] = True
            flash('You have been successfully logged in.')
            posts = [
                {
                    'author': {'nickname': 'Jerry'},
                    'body': 'Beautiful day in Boston!'
                },
                {
                    'author': {'nickname': 'Susan'},
                    'body': 'The Avengers movie was so cool.'
                }
            ]            
            return render_template('index.html',
                                    title='Home',
                                    user=user,
                                    posts=posts)
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':    
        user = User(request.form['nickname'], request.form['email'], request.form['password'])
        db.session.add(user)
        print user
        db.session.commit()
        flash('You have been successfully registered. Please login.')
        return redirect('/login')
    return render_template('register.html', error=error)        

def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, rememember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))