from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'pass123':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('index'))
    return render_template('login.html')
        
@app.route('/success')
def success():
    return 'Logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)