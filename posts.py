import requests
import os
from flask import Flask, jsonify,request,make_response
import json

app = Flask(__name__)
#app.config['SECRET_KEY'] = os.urandom(28)

port = int(os.environ.get('PORT',4500))
BASE_URL ="https://dummyjson.com"

@app.route('/posts',methods =['GET'])
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code != 200:
        return jsonify({'error': response.json()['message']}),response.status_code
    posts = []
    for post in response.json()['posts']:
        post_details = {
            'id': post['id'],
            'title': post['title']
        }
        posts.append(post_details)
    return jsonify({'details':posts}),200 if posts else 204  

@app.route("/")
def welcome():
    return "Welcome to Demo Microservice!!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=port)
   # app.run()




