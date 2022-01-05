"""
app.py
Samuel Lee
11/29/2021

flask app for downloading and converting youtube videos to mp3
via a browser
"""
from flask import Flask, request, render_template, url_for, flash, redirect, send_from_directory
from multiprocessing import Process
import os
import re
import dlp


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


os.makedirs('music/', exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def root():
        if request.method == 'POST':
            urls = request.form['urls']
            if not urls:
                flash('Enter a URL!')
            urls = urls.splitlines()
            urls, err = check_urls(urls)
            if err:
                flash(f'There were some error URLs, ignoring them:\n{err}')
            if urls:
                p = Process(target=dlp.start, args=(urls,), daemon=False)      
                p.start()

        return render_template('root.html')


@app.route('/list')
def _list():
    files = os.listdir(path='music/')
    return render_template('list.html', files=files)


@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory('music/', filename, as_attachment=True)


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