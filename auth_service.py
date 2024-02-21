from flask import Flask,request

app = Flask(__name__)

@app.route('/signup',methods=['POST'])
def signUp():
  #  student_details = request.json
    return "Student successfully signed up!!!"

@app.route('/students/1',methods=['GET'])
def get_studentdetails():
    return "1st Student details!!"


if __name__=='__main__':
    app.run()    
