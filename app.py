from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "INFO52170 Assessment 8 — Cloud Migration Demo (Sprint 0)"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
