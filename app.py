from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hallo Azure! 👋</h1><p>Das ist meine erste Python Web App.</p><p>Das ist ein Test um das Continuous Deployment zu testen!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
