from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Service running"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/version")
def version():
    try:
        commit = subprocess.check_output(
            ["git", "--git-dir=../.git", "--work-tree=..", "rev-parse", "--short", "HEAD"]
        ).decode("utf-8").strip()
    except Exception:
        commit = "unknown"
    return jsonify(version=commit)

