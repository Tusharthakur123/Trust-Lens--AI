def recommend_price(base_price, severity_score):
    discount = severity_score * 0.4
    final_price = base_price - (base_price * discount)
    return round(final_price, 2)
