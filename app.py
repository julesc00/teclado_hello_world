from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Item One",
                "price": 15.99
            }
        ]
    }
]


# GET all stores /store>
@app.route("/store")
def get_store_view():
    return jsonify({"stores": stores})


# GET all items in a store
@app.route("/store/<string:name>/item")
def get_items_in_store_view(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"message": "Items not found."})


# GET one item
@app.route("/store/<string:name>")
def get_item_view(name):
    for item in stores:
        if item["name"] == name:
            return jsonify(item)
    return jsonify({"message": "Item not found."})


# Create a new store
@app.route("/store/<string:name>", methods=["POST"])
def create_store_view(name):
    request_data = request.get_json()
    new_item = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_item)

    return jsonify(new_item)


# Create a new item in store
@app.route("/store/<string:name>/item", methods=["POST"])
def create_new_item_view(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)

            return jsonify(new_item)
    return jsonify({"message": "Store not found!"})


# Edit/Update an item
@app.route("/store/<string:name>/item", methods=["PUT"])
def update_item_view(name):
    pass


# Delete an item
@app.route("/store/<string:name>/item", methods=["DELETE"])
def delete_item_view(name):
    pass


app.run(port=5000)
