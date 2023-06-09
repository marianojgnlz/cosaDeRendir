from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x =1
    return "Esto si anda."
if __name__ == "__main__":
    app.run()