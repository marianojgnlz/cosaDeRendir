from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Esto si anda."
if __name__ == "__main__":
    app.run()