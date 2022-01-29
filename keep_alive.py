from flask import Flask
from threading import Thread

app = Flask("Scrappie")

url = "https://bazthedev.github.io/" # change this to any link you want

@app.route("/")
def home():
  return f"<script>window.location.href='{url}';</script>"
def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()