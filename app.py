from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Replace 'default_secret_key' with a secure value

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        posts.append({'title': title, 'content': content})
    else:
        flash("Title and Content cannot be empty")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)