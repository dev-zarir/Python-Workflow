from pyngrok import conf, ngrok
from time import sleep
from flask import Flask

conf.get_default().auth_token = "2A4kC6bPdmqWbDFFXzUgT9Dlhg1_2BpCsMEMSJJgSH4EsnqAC"

conf.get_default().region = "ap"

tunnel=ngrok.connect(80, "tcp")

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run(port=80)
