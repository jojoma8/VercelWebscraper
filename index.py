from flask import Flask, jsonify
# from flask_cors import CORS
import tg
import econ
from flask_cors import cross_origin

# import requests

app = Flask(__name__)
# cors = CORS(app, resources={r'/*': {'origins': '*'}})
app.url_map.strict_slashes = False


@app.route("/")
# @cross_origin()
def home():
    return "API is working fine 444 !"


# @app.route("/<query>")
# def telegram_(query):
#     return jsonify(tg.telegram(query))

@app.route("/<query>")
def read_(query):
    return jsonify(econ.read(query))


if __name__ == "__main__":
    # app.debug = True
    app.debug = False
    # app.run(host="0.0.0.0", port=5000)
