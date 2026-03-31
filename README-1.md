# 🔐 PassAudit — Password Strength Analyzer

A lightweight cybersecurity web app built with Python & Flask that analyzes password strength in real time. No data is stored or sent anywhere — all analysis happens on your server.

---

## Features

- **Real-time analysis** as you type
- **10-point scoring system** across multiple security criteria
- **Shannon entropy calculation** (bits of randomness)
- **Visual strength meter** with color-coded feedback
- **10 security checks** including length, character variety, repeated chars, sequential patterns, and common password detection
- **Show/hide password** toggle
- Zero external dependencies beyond Flask

---

## Screenshots

> Run the app locally and visit `http://127.0.0.1:5000`

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/passaudit.git
cd passaudit
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open your browser and go to: `http://127.0.0.1:5000`

---

## How Scoring Works

Each password is evaluated against 10 criteria:

| # | Check | Points |
|---|-------|--------|
| 1 | At least 8 characters | +1 |
| 2 | At least 12 characters | +1 |
| 3 | At least 16 characters | +1 |
| 4 | Contains lowercase letters | +1 |
| 5 | Contains uppercase letters | +1 |
| 6 | Contains numbers | +1 |
| 7 | Contains special characters | +1 |
| 8 | No repeated characters (aaa) | +1 |
| 9 | No sequential patterns (123, abc) | +1 |
| 10 | Not a common password | +1 |

**Score → Rating:**

| Score | Rating |
|-------|--------|
| 0–2   | Very Weak |
| 3–4   | Weak |
| 5–6   | Fair |
| 7–8   | Strong |
| 9–10  | Very Strong |

### Entropy

Entropy is calculated using:

```
Entropy = len(password) × log₂(charset_size)
```

Where `charset_size` is the number of unique character types used (lowercase, uppercase, digits, symbols).

---

## Project Structure

```
passaudit/
├── app.py               # Flask backend & password analysis logic
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Frontend (HTML/CSS/JS)
└── README.md
```

---

## Security Notes

- Passwords are **never logged, stored, or transmitted** to any third party.
- All analysis is performed in-memory on the server handling the request.
- For production use, serve behind HTTPS and disable Flask debug mode.

---

## Contributing

Pull requests are welcome! Some ideas for extension:

- [ ] HaveIBeenPwned API integration (check breach databases)
- [ ] Password generator tool
- [ ] Passphrase strength support
- [ ] Dark/light theme toggle
- [ ] CLI version

---

## License

MIT License — see [LICENSE](LICENSE) for details.
