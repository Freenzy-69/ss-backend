from flask import Flask, request

app = Flask(__name__)
scripts = {}

@app.route("/api/send", methods=["POST"])
def send_script():
    uid = request.args.get("id")
    script = request.form.get("script")
    scripts[uid] = script
    return "OK"

@app.route("/cdn", methods=["GET"])
def get_script():
    uid = request.args.get("id")
    return scripts.get(uid, "-- Nenhum script encontrado")

@app.route("/", methods=["GET"])
def home():
    return "Server Side funcionando!"
