from flask import Flask, request

app = Flask(__name__)

bookstores = [
    {
        "name": "Asian Book Store",
        "books": [
            {
                "name": "Python",
                "publication": "Oreally"
            }
        ]
    }
]

@app.get("/bookstore")
def get_bookstores():
    return {"stores": bookstores}


@app.post("/newbookstore")
def create_book_store():
    request_data = request.get_json()
    new_book_store = {"name": request_data["name"], "books": []}
    bookstores.append(new_book_store)
    return new_book_store, 201


@app.post("/bookstore/<string:name>/book")
def create_book_item(name):
    request_data = request.get_json()
    for store in bookstores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "publication": request_data["publication"]}
            store["books"].append(new_item)
            return new_item, 201
    return {"message": "Book Store not found"}, 404


@app.get("/bookstore/<string:name>")
def get_book_store(name):
    for store in bookstores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/book")
def get_item_in_book_store(name):
    for store in bookstores:
        if store["name"] == name:
            return {"books": store["book"]}
    return {"message": "Book Store not found"}, 404

if __name__ == '__main__':
    app.run(port=4500)
