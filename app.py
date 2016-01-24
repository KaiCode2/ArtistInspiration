
from flask import Flask, render_template
from Concept import Concept

app = Flask(__name__)

@app.route("/")
def index():
    c = Concept()
    return render_template("index.html", inspiration=c.conceptualize())

@app.route("/<string:subject>/<string:descriptor>/<string:setting>/")
def concept_route(subject, descriptor, setting):
    print subject, descriptor, setting
    c = Concept([subject, descriptor, setting])
    return render_template("index.html", inspiration=c.conceptualize())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
