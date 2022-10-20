from flask import Flask
from flask_ngrok2 import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app, auth_token="2A4kC6bPdmqWbDFFXzUgT9Dlhg1_2BpCsMEMSJJgSH4EsnqAC")

@app.route("/")
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run()
