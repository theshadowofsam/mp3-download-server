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
    r = requests.get(url[1], allow_redirects=True)
    print(r)

if __name__ == "__main__":
    main("https://www.youtube.com/watch?v=kGxiZNbjwGI")