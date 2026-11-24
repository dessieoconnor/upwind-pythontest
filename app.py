from flask import Flask, request
from sanitiser import clean_input



app = Flask(__name__)

@app.route("/hello")
def hello():
    user_input = request.args.get("name", "")
    safe_input = clean_input(user_input)
    return f"<h1>Hello {safe_input}</h1>"



if __name__ == "__main__":
    app.run(port=5000)
