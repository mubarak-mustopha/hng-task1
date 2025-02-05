from decouple import config
from flask import Flask, render_template, request, jsonify

from utils import get_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/classify-number")
def classify_number():
    number = request.args.get("number")
    try:
        data, status = get_data(int(number)), 200
    except (ValueError, TypeError) as e:
        print(e)
        data, status = {"number": number, "error": True}, 400

    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response, status


if __name__ == "__main__":
    if debug := config("DEBUG", cast=bool):
        app.run(host="0.0.0.0", port=8000, debug=debug)
    else:
        app.run()
