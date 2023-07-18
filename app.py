from flask import Flask
import flask_cors
import os


app = Flask(__name__)
flask_cors.CORS(app)
port = int(os.environ.get("PORT", 5000))


@app.route("/ping")
def update_totals():
    return "pong"
