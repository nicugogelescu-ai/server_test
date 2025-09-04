import os
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Python HTTPS server is online on Render!"

@app.route("/ro", methods=["GET"])
def get_file():
    # send a file to the client
    return send_file("fisier_test.txt", as_attachment=True)

@app.route("/al", methods=["GET"])
def get_file():
    # send a file to the client
    return send_file("fisier_test.txt", as_attachment=True)

@app.route("/hello", methods=["GET"])
def hello():
    # JSON response
    return jsonify({"message": "Hello, curl client from Render!"})

@app.route("/upload", methods=["POST"])
def upload():
    # receive file from client
    if "file" not in request.files:
        return "No file uploaded!", 400
    f = request.files["file"]
    f.save(f.filename)
    return f"File '{f.filename}' successfully saved!"

if __name__ == "__main__":
    # Render sets PORT as an environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
