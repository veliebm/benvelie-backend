from flask import Flask
import flask_cors
import os


app = Flask(__name__)


def main():
    flask_cors.CORS(app)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)


@app.route("/ping")
def update_totals():
    return "pong"


if __name__ == "__main__":
    main()
