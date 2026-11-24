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


@app.route("/download")
def download():
    filename = request.args.get("file")
    return send_file("/var/data/" + filename)     # path traversal


@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    return requests.get(url, verify=False).text   # SSRF + TLS verification disabled


@app.route("/go")
def go():
    return redirect(request.args.get("next"))     # open redirect


@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    return render_template_string("<h1>Hello " + name + "</h1>")   # XSS / template injection


@app.route("/xml", methods=["POST"])
def parse_xml():
    return ET.fromstring(request.data).tag        # XML parsing of untrusted input


@app.route("/xml2", methods=["POST"])
def parse_xml2():
    return minidom.parseString(request.data).toxml()   # XXE-prone parser


@app.route("/token")
def token():
    return jwt.encode({"user": "admin"}, JWT_SECRET, algorithm="HS256")


@app.route("/decode")
def decode():
    return str(jwt.decode(request.args.get("t"), options={"verify_signature": False}))  # JWT signature not verified


def make_token():
    return str(random.randint(100000, 999999))    # insecure randomness for a security token


def hash_password(pw):
    return hashlib.sha1(pw.encode()).hexdigest()  # weak hash


def encrypt(data):
    return DES.new(b"8bytekey", DES.MODE_ECB).encrypt(data)   # weak cipher + ECB


def temp_file():
    return tempfile.mktemp()                      # insecure temp file


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)        
