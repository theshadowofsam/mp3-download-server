"""
app.py
Samuel Lee
11/29/2021
"""
from flask import Flask
from flask import request
import dlp

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        return ""
    else:
        return "127.0.0.1:5000"


if __name__ == '__main__':
    app.run()