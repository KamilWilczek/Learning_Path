import datetime
import requests
from requests_html import HTML

now = datetime.datetime.now()
year = now.year


def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", "w", encoding="utf-8") as f:
                f.write(html_text)
        return html_text
    return ""


url = "https://www.boxofficemojo.com/year/world/"

html_text = url_to_txt(url)

r_html = HTML(html=html_text)
table_class = "a-section imdb-scroll-table mojo-gutter imdb-scroll-table-styles"
r_table = r_html.find(table_class)

print(r_table)
