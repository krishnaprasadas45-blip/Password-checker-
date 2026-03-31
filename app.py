from flask import Flask, render_template, request, jsonify
import re
import math

app = Flask(__name__)


def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'[0-9]', password):
        charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset += 32
    if charset == 0:
        return 0
    return len(password) * math.log2(charset)


def check_strength(password):
    if not password:
        return {"score": 0, "label": "Empty", "color": "empty", "checks": [], "entropy": 0}

    checks = []
    score = 0

    # Length checks
    length = len(password)
    if length >= 8:
        score += 1
        checks.append({"label": "At least 8 characters", "passed": True})
    else:
        checks.append({"label": "At least 8 characters", "passed": False})

    if length >= 12:
        score += 1
        checks.append({"label": "At least 12 characters", "passed": True})
    else:
        checks.append({"label": "At least 12 characters", "passed": False})

    if length >= 16:
        score += 1
        checks.append({"label": "At least 16 characters", "passed": True})
    else:
        checks.append({"label": "At least 16 characters", "passed": False})

    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
        checks.append({"label": "Lowercase letters (a–z)", "passed": True})
    else:
        checks.append({"label": "Lowercase letters (a–z)", "passed": False})

    if re.search(r'[A-Z]', password):
        score += 1
        checks.append({"label": "Uppercase letters (A–Z)", "passed": True})
    else:
        checks.append({"label": "Uppercase letters (A–Z)", "passed": False})

    if re.search(r'[0-9]', password):
        score += 1
        checks.append({"label": "Numbers (0–9)", "passed": True})
    else:
        checks.append({"label": "Numbers (0–9)", "passed": False})

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        checks.append({"label": "Special characters (!@#...)", "passed": True})
    else:
        checks.append({"label": "Special characters (!@#...)", "passed": False})

    # Pattern checks
    if not re.search(r'(.)\1{2,}', password):
        score += 1
        checks.append({"label": "No repeated characters (aaa)", "passed": True})
    else:
        checks.append({"label": "No repeated characters (aaa)", "passed": False})

    if not re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg)', password.lower()):
        score += 1
        checks.append({"label": "No sequential patterns (123, abc)", "passed": True})
    else:
        checks.append({"label": "No sequential patterns (123, abc)", "passed": False})

    common_passwords = ['password', '123456', 'qwerty', 'letmein', 'admin', 'welcome', 'monkey', 'dragon']
    if password.lower() not in common_passwords:
        score += 1
        checks.append({"label": "Not a common password", "passed": True})
    else:
        checks.append({"label": "Not a common password", "passed": False})

    # Score to label
    max_score = 10
    percentage = (score / max_score) * 100

    if score <= 2:
        label, color = "Very Weak", "very-weak"
    elif score <= 4:
        label, color = "Weak", "weak"
    elif score <= 6:
        label, color = "Fair", "fair"
    elif score <= 8:
        label, color = "Strong", "strong"
    else:
        label, color = "Very Strong", "very-strong"

    entropy = round(calculate_entropy(password), 1)

    return {
        "score": score,
        "max_score": max_score,
        "percentage": percentage,
        "label": label,
        "color": color,
        "checks": checks,
        "entropy": entropy,
        "length": length
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result = check_strength(password)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
