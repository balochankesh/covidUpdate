from flask import Flask,request,jsonify,redirect,render_template,url_for
import requests



app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():

    if request.method == "POST":
        se = request.form["state"]

        try:
            return redirect(url_for("state",state=se))

        except requests.exceptions.RequestException as e:
            return redirect(url_for("home"))
    else:
        return render_template("home.html")


@app.route("/<state>/")
def state(state):
    data = requests.get("https://souravcovid19api.herokuapp.com/api/state/"+state)
    r= data.json()

    name = r["Name"]
    conf = r["Confirmed"]
    deaths = r["Death"]
    cured = r["Cured"]

    return render_template("state.html", state=name,conf=conf,deaths=deaths,cured=cured)

if __name__ == "__main__":
    app.run(debug=True)



