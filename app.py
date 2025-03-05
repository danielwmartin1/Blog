from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Replace 'default_secret_key' with a secure value
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    # Debugging information
    app.logger.debug(f"Received title: {title}")
    app.logger.debug(f"Received content: {content}")
    app.logger.debug(f"Received author: {author}")
    
    # Validation
    if not title or not content or not author:
        flash("Title, Content, and Author cannot be empty", "error")
        return redirect(url_for('index'))
    
    if len(title) < 5:
        flash("Title must be at least 5 characters long", "error")
        return redirect(url_for('index'))
    
    if len(content) < 10:
        flash("Content must be at least 10 characters long", "error")
        return redirect(url_for('index'))
    
    if len(author) < 2:
        flash("Author must be at least 2 characters long", "error")
        return redirect(url_for('index'))
    
    new_post = Post(title=title, content=content, author=author)
    db.session.add(new_post)
    db.session.commit()
    flash("Post added successfully", "success")
    return redirect(url_for('index'))

@app.route('/delete-post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully", "success")
    return '', 204

@app.route('/update-post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post_data = request.get_json()
    post = Post.query.get_or_404(post_id)
    post.title = post_data.get('title', post.title)
    post.content = post_data.get('content', post.content)
    post.author = post_data.get('author', post.author)
    db.session.commit()
    flash("Post updated successfully", "success")
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)  # Change the port number to 5001 or any other available port