from flask import Flask, render_template
from goal_horn import play_sequence, stop_sequence
import threading

import os
from flask import Flask

app = Flask(__name__, template_folder="templates", static_folder="static")

# Secret key (used for sessions, login, etc.)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    threading.Thread(target=play_sequence).start()
    return "Horn Started"

@app.route("/stop")
def stop():
    stop_sequence()
    return "Horn stopped"

if __name__ == "__main__":
    app.run(debug=True)