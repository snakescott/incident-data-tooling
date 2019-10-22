import requests
import urllib


def is_statuspageio_domain(domain: str) -> bool:
    url = urllib.parse.urlunparse(("https", domain, "api/v2/status.json", "", "", ""))
    try:
        result = requests.get(url, timeout=5).json()
    except RuntimeError:
        return False
    return isinstance(result, dict) and "page" in result and "id" in result["page"]
