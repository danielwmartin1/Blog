from flask import Flask, request, redirect, url_for, flash, render_template
from models import Post, db

app = Flask(__name__)

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    author = 'Dan'  # You can modify this to get the actual author
    new_post = Post(title=title, content=content, author=author)
    db.session.add(new_post)
    db.session.commit()
    flash('Post added successfully!')
    return redirect(url_for('index'))

@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!')
    return '', 204

# ...existing code...
