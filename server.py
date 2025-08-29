import os
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Server HTTPS Python este online pe Render!"

@app.route("/get_file", methods=["GET"])
def get_file():
    # trimite un fișier către client
    return send_file("fisier_test.txt", as_attachment=True)

@app.route("/hello", methods=["GET"])
def hello():
    # răspuns JSON
    return jsonify({"mesaj": "Salut, client curl de pe Render!"})

@app.route("/upload", methods=["POST"])
def upload():
    # primește fișier de la client
    if "file" not in request.files:
        return "Niciun fișier trimis!", 400
    f = request.files["file"]
    f.save(f.filename)
    return f"Fișier '{f.filename}' salvat cu succes!"

if __name__ == "__main__":
    # Render setează PORT ca variabilă de mediu
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
