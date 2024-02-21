import requests
import os
from flask import Flask, jsonify,request,make_response
import jwt
from functools import wraps
import json
from jwt.exceptions import DecodeError

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(28)

port = int(os.environ.get('PORT',4500))
BASE_URL ="https://dummyjson.com"

def token_generate(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token =request.cookies.get('token')
        if not token:
            return jsonify({'error': 'Need Authorization token'}),401
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user_id = data['user_id']
        except DecodeError:
            return jsonify({'error':'Invalid token'}),401
        return f(current_user_id,*args,**kwargs)
    return decorated

with open('users.json','r') as f:
    users=json.load(f)

@app.route('/auth',methods=['POST'])
def authenticate_user():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error':'Unsupported Content type'}),415
    username = request.json.get('username')
    password = request.json.get('password')
    
    for u in users:
        if u['username']==username and u['password'] == password:
            token =jwt.encode({'user_id': u['id']},app.config['SECRET_KEY'],algorithm="HS256")
            response=make_response(jsonify({'message':'Successfully Authenticated'}))
            response.set_cookie('token',token)
            return response, 200
    return jsonify({'error': 'Invalid username or password'}),401

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




