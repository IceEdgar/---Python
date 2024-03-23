import requests

S = requests.Session()


def get_sites(lat, long, radius, limit=100):
    URL = "https://en.wikipedia.org/w/api.php"
    params = {
    "action": "query",
    "format": "json",
    "list": "geosearch",
    "gscoord": f"{lat}|{long}",
    "gsradius": f"{radius}",
    "gslimit": f"{limit}"
    }
    r = S.get(url=URL, params=params)
    pages = r.json()["query"]["geosearch"]
    sites = [i["title"] for i in pages]
    return sites


def test_step1(text, coord):
    assert text in get_sites(coord[0], coord[1], 100), "not found"
