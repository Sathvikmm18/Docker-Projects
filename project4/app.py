from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>It's a Dockerized a simple python flask web application running in 5000 port"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    