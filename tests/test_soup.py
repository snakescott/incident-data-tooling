from bs4 import BeautifulSoup
from urllib.parse import urlparse
from idt.soup import parse_link
import pytest


@pytest.fixture
def bs():
    return BeautifulSoup(features="html.parser")


@pytest.mark.parametrize("href", [None, "https://www.foo.com/bar"])
def test_parse_link(bs, href):
    new_link = bs.new_tag("a", href=href)

    if href:
        assert parse_link(new_link) == urlparse(href)
    else:
        assert parse_link(new_link) is None
