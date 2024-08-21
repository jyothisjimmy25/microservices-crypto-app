from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# Generate a secure random key for signing session cookies
app.secret_key = os.urandom(24)

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "password123"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            session['username'] = username
            return redirect("http://127.0.0.1:5001/products")  # Redirect to the microservice
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
