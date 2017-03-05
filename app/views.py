from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Rachel'}
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