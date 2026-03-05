from flask import Flask, render_template, request, jsonify
import json, os

app = Flask(__name__)

DB_FILE = "players.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE,"w") as f:
        json.dump({}, f)

def load_players():
    with open(DB_FILE) as f:
        return json.load(f)

def save_players(data):
    with open(DB_FILE,"w") as f:
        json.dump(data, f)

@app.route("/")
def game():
    return render_template("index.html")

@app.route("/tap", methods=["POST"])
def tap():
    user = request.json["user"]
    players = load_players()
    if user not in players:
        players[user] = 0
    players[user] += 1
    save_players(players)
    return jsonify({"coins": players[user]})

@app.route("/balance/<user>")
def balance(user):
    players = load_players()
    coins = players.get(user,0)
    return jsonify({"coins": coins})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
