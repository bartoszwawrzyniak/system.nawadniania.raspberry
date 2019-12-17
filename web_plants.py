from flask import Flask, render_template, redirect, url_for, send_from_directory
import psutil
import datetime
import water
import os

app = Flask(__name__)

def template(title = "System nawadniania Wawrzyniak Bartosz", text = ""):
    now = datetime.datetime.now()
    timeString = now
    templateDate = {
        "title" : title,
        "time" : timeString,
        "text" : text
        }
    return templateDate

@app.route("/")
def hello():
    templateData = template()
    return render_template("main.html", **templateData)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/x-icon")
						  
@app.route("/last_watered")
def check_last_watered():
    templateData = template(text = water.get_last_watered())
    return render_template("main.html", **templateData)

@app.route("/sensor")
def action():
    status = water.get_status()
    message = ""
    if (status == 1):
        message = "Potrzebuje wody!"
    else:
        message = "Jestem szczesliwa roslina"

    templateData = template(text = message)
    return render_template("main.html", **templateData)

@app.route("/water")
def action2():
    water.pump_on()
    templateData = template(text = "Podlewanie")
    return render_template("main.html", **templateData)

@app.route("/water_off")
def action3():
    water.pump_off()
    templateData = template(text = "Koniec podlewania")
    return render_template("main.html", **templateData)


@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        templateData = template(text = "Automatyczne podlewanie On")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == "auto_water.py":
                    templateData = template(text = "uruchomiono")
                    running = True
            except:
                pass
        if not running:
            os.system("python3 auto_water.py&")
    else:
        templateData = template(text = "Automatyczne podlewanie Off")
        os.system("pkill -f auto_water.py")

    return render_template("main.html", **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
