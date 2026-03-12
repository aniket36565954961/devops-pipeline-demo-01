from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DevOps CI/CD Pipeline Demo 🚀"

@app.route("/version")
def version():
    return "Application Version 1.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)