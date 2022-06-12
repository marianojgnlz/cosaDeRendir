from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Esto es un cambio"
if __name__ == "__main__":
    app.run()