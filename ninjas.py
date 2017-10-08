from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("home.html")

@app.route('/ninja')
def about():
    return render_template("ninja.html")

@app.route('/ninja/blue')
def blue():
    return render_template("blue.html")

@app.route('/ninja/red')
def red():
    return render_template("red.html")

@app.route('/ninja/orange')
def orange():
    return render_template("orange.html")

@app.route('/ninja/purple')
def purple():
    return render_template("purple.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug = True)