from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Upload a Video</h2>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    """

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save("Uploads/" + file.filename)
    return f"{file.filename} uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)