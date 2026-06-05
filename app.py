from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "fdd18e60e0b294c972062ee5769e0c20"

@app.route("/", methods=["GET", "POST"])
def weather():

    data = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)