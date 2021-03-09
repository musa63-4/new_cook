from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)


@app.route("/")
def top():
    return render_template("top.html")


@app.route("/butabara_moyashi.html")
def butabara_moyash():
    return render_template("butabara_moyashi.html")

@app.route("/omurice.html")
def omurice():
    return render_template("omurice.html")


@app.route("/rizot.html")
def rizot():
    return render_template("rizot.html")

@app.route("/saba_tomato_nikomi.html")
def saba_tomato_nikomi():
    return render_template("saba_tomato_nikomi.html")

@app.route("/pork_curry.html")
def pork_curry():
    return render_template("pork_curry.html")

@app.route("/sabamiso_udon.html")
def sabamiso_udon():
    return render_template("sabamiso_udon.html")

@app.route("/mugen_cabetsu.html")
def mugen_cabetsu():
    return render_template("mugen_cabetsu.html")

@app.route("/sabakantomato.html")
def sabakantomato():
    return render_template("sabakantomato.html")

@app.route("/tuna_limon_rizot.html")
def tuna_limon_rizot():
    return render_template("tuna_limon_rizot.html")



@app.route("/ninjin_salad.html")
def ninjin_salad():
    return render_template("ninjin_salad.html")

@app.route("/moyashi_namuru.html")
def moyashi():
    return render_template("moyashi_namuru.html")

@app.route("/tuna_ohitashi.html")
def tuna_ohitashi():
    return render_template("tuna_ohitashi.html")

@app.route("/meat_ball.html")
def meatball():
    return render_template("meat_ball.html")

@app.route("/renji_pasta.html")
def renji_pasta():
    return render_template("renji_pasta.html")

@app.route("/karubo_meshi.html")
def karubo_meshi():
    return render_template("karubo_meshi.html")

@app.route("/toumyou_buta.html")
def toumyou():
    return render_template("toumyou_buta.html")

@app.route("/nikudoufu.html")
def nikudoufu():
    return render_template("nikudoufu.html")

@app.route("/tonpei.html")
def tonpei():
    return render_template("tonpei.html")

@app.route("/butakyabetu.html")
def butakyabetu():
    return render_template("butakyabetu.html")

@app.route("/okonomiyaki.html")
def okonomiyaki():
    return render_template("okonomiyaki.html")






if __name__ == '__main__':
    app.run(debug=True)
