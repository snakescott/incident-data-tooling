import markdown2
from bs4 import BeautifulSoup
from typing import Set
from idt.soup import parse_link

URL = "https://raw.githubusercontent.com/danluu/post-mortems/master/README.md"


def extract_domains(text: str) -> Set[str]:
    html = markdown2.markdown(text)
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    return set(t[0] for t in filter(None, (parse_link(l) for l in links)))
