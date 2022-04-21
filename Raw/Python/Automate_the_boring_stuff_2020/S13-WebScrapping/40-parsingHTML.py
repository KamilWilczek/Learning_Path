import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

res = requests.get('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna', headers=headers)
# res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup.select('document.querySelector("#main-page-didyouknow > p:nth-child(6) > b > a")')