from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products), 200

    return jsonify(products), 200

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)