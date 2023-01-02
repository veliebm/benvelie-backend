from flask import Flask, request
import sqlite3
import json


MAX_CLICK_RATE = 16
DATABASE_PATH = "totals.db"


with sqlite3.connect("totals.db") as connection:
    for query in [
        "CREATE TABLE IF NOT EXISTS totals (id INTEGER PRIMARY KEY, click_count INTEGER NOT NULL DEFAULT 0, observation_time INTEGER NOT NULL DEFAULT 0);",
        "INSERT OR IGNORE INTO totals VALUES(1,0,0);",
    ]:
        connection.execute(query)

app = Flask(__name__)


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

    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE totals SET click_count = click_count + {incoming_click_count}, observation_time = observation_time + 1 WHERE id = 1;"
        )
        cursor.execute("SELECT click_count, observation_time FROM totals WHERE id = 1;")
        click_count, observation_time = cursor.fetchone()
        cursor.close()

    return json.dumps(
        {"click_count": click_count, "observation_time": observation_time}
    )
