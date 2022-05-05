from flask import Flask

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=["GET"])
def hello_world():
    # run other code here
    return "Hello, world. This is Flask"


# http://localhost:8000/abc
@app.route("/abc", methods=["GET"])
def abc_view():
    # run other code here
    return "Hello, world. This is abc"
