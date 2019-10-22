import requests
import urllib
import markdown2
from typing import List
from html.parser import HTMLParser

URL = "https://raw.githubusercontent.com/danluu/post-mortems/master/README.md"


class LinkParser(HTMLParser):
    def __init__(self, dest):
        super().__init__()
        self.dest = dest

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    parsed = urllib.parse.urlparse(value)
                    if parsed and parsed[1]:
                        self.dest.add(parsed[1])


def extract_domains(text: str) -> List[str]:
    html = markdown2.markdown(text)
    domains = set()
    parser = LinkParser(domains)
    parser.feed(html)
    return sorted(domains)
