from flask import Flask, request, make_response
import gamestate as game

app = Flask(__name__)

cookie_key = "sessionId"

@app.route("/")
def root():
    return "Hello, world"

'''All API routes should return JSON'''

@app.route("/api")
def api():
    return {
        "status": "online",
    }, 200

@app.route("/api/auth")
def auth():
    id = request.cookies.get(cookie_key)
    authed = game.checkSesh(int(id)) if id != None else False
    return {
        "isAuthed": authed,
    }, 200 if authed else 401

@app.route("/api/createplayer", methods=["GET", "POST"])
def apiCreatePlayer():
    if request.method != "POST":
        return {
            "message": "invalid method",
        }, 405

    data = request.get_json(silent=True)
    if data == None:
        return {
            "message": "bad media",
        }, 415

    id = request.cookies.get(cookie_key)
    if id != None:
        if game.checkSesh(int(id)):
            return {
                "message": "User already exists",
            }, 400

    name = data.get("uname")
    if name == None:
        return {
            "message": "No Name",
        }, 400

    id = game.createPlayer(name)
    resp = make_response({"message": f"{name} created successfully"}, 201)
    resp.set_cookie(cookie_key, str(id))
    print(f"USER CREATED: {game.players[id].name}")
    return resp

@app.route("/api/distance", methods=["GET", "POST"])
def apiPostDistance():
    if request.method != "POST":
        return {
            "message": "invalid method",
        }, 405

    data = request.get_json(silent=True)
    if data == None:
        return {
            "message": "bad media",
        }, 415

    id = request.cookies.get(cookie_key)
    if id == None or game.checkSesh(int(id) == False):
        return {
            "message": "Unauthorized",
        }, 401

    guess = data.get("guess")
    if guess == None:
        return {
            "message": "No guess",
        }, 400

    r = game.handleGuess(guess)
    return {
        "distance": r[0],
        "finished": r[1]
    }, 200
