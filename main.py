from pyngrok import conf, ngrok
from time import sleep
from flask import Flask
from threading import Thread

def web():
    app=Flask(__name__)
    
    @app.route("/")
    def home():
        return "Hello World!"
    
    app.run()

t=Thread(target=web)
t.daemon=True
t.start()

conf.get_default().auth_token = "2A4kC6bPdmqWbDFFXzUgT9Dlhg1_2BpCsMEMSJJgSH4EsnqAC"

conf.get_default().region = "ap"

while True:
    tunnel=ngrok.connect(5000, "tcp")
    print(tunnel.public_url.replace("tcp://",""))
    sleep(60)
    ngrok.kill()
