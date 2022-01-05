"""
app.py
Samuel Lee
11/29/2021
"""
from flask import Flask, request, render_template, url_for, flash, redirect
import dlp
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

@app.route('/', methods=['GET', 'POST'])
def root():
        if request.method == 'POST':
            pass
        
        return render_template('root.html')


if __name__ == '__main__':
    app.run()