"""
server.py
Samuel Lee
11/29/2021
"""
import requests
import yt_search
import asyncio

format = 250

def main(url):
    url = yt_search.search(url)
    r = requests.get(url[1], allow_redirects=True, stream=True)
    print(r)

    with open("audio.weba", 'wb') as fd:
        for i in r.iter_content():
            fd.write(i)

if __name__ == "__main__":
    main("https://www.youtube.com/watch?v=kGxiZNbjwGI")