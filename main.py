
import subprocess
import sys
import time
import re
import os
import requests
import threading
import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, I'm your Flask app!"
port = int(os.environ.get("PORT", 5000))
def flask_thread():
    app.run(host="0.0.0.0", port=port)





if __name__ == "__main__":
    # Create and start the Flask thread
    flask_thread = threading.Thread(target=flask_thread)
    flask_thread.start()

