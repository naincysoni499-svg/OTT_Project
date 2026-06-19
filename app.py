from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return """
    <h1>OTT Video Upload Portal</h1>
    <p>Supported formats: MP4, AVI, MOV</p>

    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload Video</button>
    </form>
    """

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file.filename == "":
        return "No file selected!"

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return f"{file.filename} uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)