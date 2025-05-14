from flask import Flask, render_template, request
import os

template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir)
#defina a pasta onde estão os aquivos html (neste caso, a raíz do projeto)

#direcionamento para base do index HTML
@app.route("/")
def home ():
    return render_template("index.html")

if __name__ ==  "__main__":
    app.run(host = "0.0.0.0", port=3000)