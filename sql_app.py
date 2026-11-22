
from flask import Flask, request
from sql_database import find_user

app = Flask(__name__)

@app.route("/user")
def user():
    username = request.args.get("username", "")
    return {"results": find_user(username)}

if __name__ == "__main__":
    app.run(port=5001)
