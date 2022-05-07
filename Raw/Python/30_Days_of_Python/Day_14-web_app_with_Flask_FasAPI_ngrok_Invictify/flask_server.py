from flask import Flask
from numpy import tri

from logger import trigger_log_save
from scrape import run as scrape_runner

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


# http://localhost:8000/box-office-mojo-scrapper
@app.route("/box-office-mojo-scrapper", methods=["POST"])
def box_office_scrapper_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1, 2, 3]}
