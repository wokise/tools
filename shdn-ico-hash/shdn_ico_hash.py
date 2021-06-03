import sys
import mmh3
import codecs
from requests_html import HTMLSession


requests = HTMLSession()


def update_favicon_url(url):
    img_ext = ['ico', 'png', 'apng', 'gif', 'jpg', 'jfif', 'jpe', 'jpeg', 'svg', 'svgz']
    url_ext = url.split('.')[-1]
    if url_ext not in img_ext:
        response = requests.get(url)
        icon = response.html.find('link[type="image/x-icon"]', first=True)
        url = f"{url}{icon.attrs['href']}"
    return url


def get_favicon_hash(url):
    response = requests.get(url)
    fav = codecs.encode(response.content, "base64")
    fav_hash = mmh3.hash(fav)
    return fav_hash


if __name__ == "__main__":
    if sys.argv[1:]:
        fav_url = sys.argv[1]
        fav_url = update_favicon_url(fav_url)
        fav_hash = get_favicon_hash(fav_url)
        print(f'http.favicon.hash:{abs(fav_hash)}')
