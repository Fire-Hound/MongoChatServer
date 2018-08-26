import flask 
import pymongo
app = flask.Flask(__name__)
app.secret_key = "any random string"
#chats = [{"user":"vikram", "text":"Hello Chat"}]
client = pymongo.MongoClient("localhost:40009")
db = client.ChatDB
collection = db.chats

@app.route("/login", methods=["POST", "GET"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        flask.session["username"] = username
        return flask.redirect(flask.url_for("getChatPage"))
    return flask.render_template("login.html")

@app.route("/", methods=["POST", "GET"])
def getChatPage():  
    if "username" in flask.session:
        user = flask.session["username"]
    else:
        return flask.redirect(flask.url_for("login"))
    if flask.request.method == "POST":
        text = flask.request.form['text']
        collection.insert_one({"user":user, "text":text})
    chats = list(collection.find())
    return flask.render_template("chatPage.html", chats=chats)
app.run('0.0.0.0', port=40010)
client.close()