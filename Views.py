from flask import Flask, request, redirect, url_for, flash, render_template
from models import Post

app = Flask(__name__)

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    author = 'Dan'  # You can modify this to get the actual author
    new_post = Post(title=title, content=content, author=author)
    # Save the new post to the database
    # ...existing code to save the post...
    flash('Post added successfully!')
    return redirect(url_for('index'))

# ...existing code...
