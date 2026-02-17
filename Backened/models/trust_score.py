def calculate_trust(seller_rating, fraud_score):
    trust = (seller_rating * 20) * (1 - fraud_score)
    return round(trust, 2)
