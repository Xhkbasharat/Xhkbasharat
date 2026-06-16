from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Sample product catalog
products = pd.DataFrame({
    "product_id": [1, 2, 3, 4],
    "name": ["Laptop", "Gaming Mouse", "Mechanical Keyboard", "Monitor"],
    "electronics": [1, 1, 1, 1],
    "gaming": [0, 1, 1, 0],
    "office": [1, 0, 1, 1],
})

feature_cols = ["electronics", "gaming", "office"]

@app.get("/")
def home():
    return {
        "message": "Smart E-Commerce Recommendation Engine API",
        "endpoint": "/recommend?product_id=<id>"
    }

@app.get("/recommend")
def recommend():
    try:
        product_id = int(request.args.get("product_id", "1"))
    except ValueError:
        return jsonify({"error": "Invalid product_id"}), 400

    if product_id not in products["product_id"].values:
        return jsonify({"error": "Product not found"}), 404

    sim = cosine_similarity(products[feature_cols])
    idx = products.index[products["product_id"] == product_id][0]
    scores = list(enumerate(sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recs = []
    for i, score in scores[1:4]:
        recs.append({
            "product_id": int(products.iloc[i]["product_id"]),
            "name": products.iloc[i]["name"],
            "similarity": round(float(score), 3)
        })

    return jsonify({
        "selected_product": product_id,
        "recommendations": recs
    })

if __name__ == "__main__":
    app.run(debug=True)