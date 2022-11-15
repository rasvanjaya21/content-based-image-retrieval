from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="templates/", static_url_path="/")
CORS(app)

@app.route("/")
@cross_origin()
def index():
    return send_from_directory(app.static_folder , "index.html")

if __name__ == '__main__':
    app.run()