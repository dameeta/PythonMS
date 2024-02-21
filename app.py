from flask import Flask
app = Flask(__name__)

@app.route('/')
def greet():
    return "Hello Students!!"

if __name__=='__main__':
    app.run()