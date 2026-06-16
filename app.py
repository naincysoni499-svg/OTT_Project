from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

@app.route("/")
def home():
    return "My OTT Project"

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return f"{file.filename} uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)
    