from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return "Welcome god4saken"


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'opey' or request.form['password'] != 'answer':
            error = 'You have entered the wrong username, password combination.'
        else:
            return redirect(url_for('welcome_page'))
    return render_template('Login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
