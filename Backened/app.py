from flask import Flask, request, jsonify
from flask_cors import CORS
from models.damage_model import analyze_damage
from models.fraud_model import check_fraud
from models.pricing_model import recommend_price
from models.trust_score import calculate_trust
from utils.nlp_generator import generate_explanation
from utils.image_processing import save_image

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]
    seller_rating = float(request.form.get("seller_rating", 4.5))
    base_price = float(request.form.get("base_price", 10000))

    image_path = save_image(file)

    damage_level, severity_score = analyze_damage(image_path)
    fraud_score = check_fraud(image_path)
    recommended_price = recommend_price(base_price, severity_score)
    trust_score = calculate_trust(seller_rating, fraud_score)
    explanation = generate_explanation(damage_level, severity_score)

    return jsonify({
        "damage_level": damage_level,
        "severity_score": severity_score,
        "fraud_score": fraud_score,
        "recommended_price": recommended_price,
        "trust_score": trust_score,
        "explanation": explanation
    })

if __name__ == "__main__":
    app.run(debug=True)
