from flask import Flask, jsonify
from flask_cors import CORS
import tg
import econ
import test
# import requests

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


@app.route("/")
def home():
    return "API is working fine 446 !"


# @app.route("/<query>")
# def scraper_(query):
#     return (test.scraper(query))


# @app.route("/sprojects")
# def telegram_():
#     return (tg.telegram())

# @app.route("/<query>")
# def telegram_(query):
#     return (tg.telegram(query))

@app.route("/<query>", methods=['GET'])
def read_(query):
    return (econ.read((f'{query}')))
    # return (econ.read('leaders/for-all-americas-success-in-helping-ukraine-hard-times-lie-ahead/21808338'))


if __name__ == "__main__":
    # app.debug = True
    app.debug = False
    # app.run(host="0.0.0.0", port=5000)
