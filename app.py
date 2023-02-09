from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
import flask_cors


MAX_CLICK_RATE = 16


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///totals.db"
flask_cors.CORS(app)

database = SQLAlchemy(app)


class Totals(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    click_count = database.Column(database.Integer)
    observation_time = database.Column(database.Integer)


with app.app_context():
    database.create_all()
    totals_already_exist = database.session.query(Totals).filter(Totals.id == 1).first()
    if not totals_already_exist:
        database.session.add(Totals(id=1, click_count=0, observation_time=0))
        database.session.commit()


@app.route("/")
def home():
    return "you're probably not supposed to be seeing this page 🧐"


@app.route("/totals")
def get_totals():
    incoming_click_count = (
        int(request.args["click_count"])
        if int(request.args["click_count"]) <= MAX_CLICK_RATE
        else MAX_CLICK_RATE
    )

    if incoming_click_count < 0:
        return "Click count can never be less than 0.", 400

    current_totals = Totals.query.all()[0]
    current_totals.click_count += incoming_click_count
    current_totals.observation_time += 1
    database.session.commit()

    return json.dumps(
        {
            "click_count": current_totals.click_count,
            "observation_time": current_totals.observation_time,
        }
    )
