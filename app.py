"""
app.py
Samuel Lee
11/29/2021


"""
from flask import Flask, request, render_template, url_for, flash, redirect
import dlp
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

@app.route('/', methods=['GET', 'POST'])
def root():
        if request.method == 'POST':
            urls = request.form['urls']
            if not urls:
                flash('Enter a URL!')
            urls = urls.splitlines()
            urls, err = check_urls(urls)
            if not err:
                flash(f'There were some error URLs, ignoring them:\n{err}')
            if urls:
                print(urls)


        return render_template('root.html')


def check_urls(urls):
    err = []
    good = []
    for url in urls:
        if url.startswith('https://www.youtube.com/watch?v=') or url.startswith('youtube.com/watch?v='):
            reg = re.search(r'watch\?v=.{11}$', url)
            if reg:
                good.append(url)
        else:
            err.append(url)
    return good, err


if __name__ == '__main__':
    app.run()