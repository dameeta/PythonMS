from flask import Flask,request
app = Flask(__name__)

bookstore = [{"name": "Asian Book Store","books":
    [{"name": "Python","Publication":"Oreally"}]}]

@app.route("/bookstore",methods=['GET'])
def get_bookstore():
    return {"bookstore":bookstore}


@app.route("/newbookstore",methods=["POST"])
def create_bookstore():
    request_data = request.get_json()
    new_book_store = {"name": request_data["name"],"books":[]}
    bookstore.append(new_book_store)
    return new_book_store,201

if __name__ == '__main__':
    app.run(port=4500)