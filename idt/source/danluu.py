import urllib
import markdown2
from bs4 import BeautifulSoup
from typing import Set

URL = "https://raw.githubusercontent.com/danluu/post-mortems/master/README.md"


def parse_domain(link):
    href = link.attrs.get("href")
    if href:
        parsed = urllib.parse.urlparse(href)
        if parsed:
            return parsed[1]
    return None


def extract_domains(text: str) -> Set[str]:
    html = markdown2.markdown(text)
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    return set(filter(None, (parse_domain(l) for l in links)))
