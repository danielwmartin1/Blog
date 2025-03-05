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
    
    posts.append({'title': title, 'content': content, 'author': author})
    flash("Post added successfully", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port number to 5001 or any other available port