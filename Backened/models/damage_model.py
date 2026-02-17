import random

def analyze_damage(image_path):
    # Simulated AI Model
    levels = ["No Damage", "Minor Cosmetic", "Moderate Damage", "Severe Damage"]
    severity_score = round(random.uniform(0, 1), 2)

    if severity_score < 0.2:
        level = levels[0]
    elif severity_score < 0.5:
        level = levels[1]
    elif severity_score < 0.8:
        level = levels[2]
    else:
        level = levels[3]

    return level, severity_score
