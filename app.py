from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def WelcomePage1():
    return render_template("index.html")

@app.route('/<name>')
def WelcomePage2(name):
    return render_template("hello.html",name=name)

if __name__ == '__main__':
    app.run()