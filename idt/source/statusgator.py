import urllib
from bs4 import BeautifulSoup
from bs4.element import Tag

URL = "https://statusgator.com"


def extract_service_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all(
        "a", attrs={"href": lambda href: href and href.startswith("/services/")}
    )
    links = [l.attrs["href"] for l in links]
    return sorted(f"{URL}{l}" for l in links)


def is_status_link(link):
    return any(
        map(
            lambda e: isinstance(e, Tag) and "fa-heartbeat" in e.attrs.get("class", []),
            link.previous_siblings,
        )
    )


def extract_status_domain(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", attrs={"target": lambda target: target == "_blank"})
    links = [l.attrs["href"] for l in links if is_status_link(l)]

    parsed = urllib.parse.urlparse(links[0])
    if parsed and parsed[1]:
        return parsed[1]

    return None
