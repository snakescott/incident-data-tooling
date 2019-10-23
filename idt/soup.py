from urllib.parse import urlparse


def parse_link(link):
    href = link.attrs.get("href")
    return href and urlparse(href)
