"""Makes a call using sat name and returns the wiki page content"""

from flask import Flask
import requests

BASE_URL = "https://en.wikipedia.org/w/api.php?action=parse&page="

FORMAT_PARAMETERS_HTML = "&format=json&prop=text&formatversion=2"
FORMAT_PARAMETERS_WIKITEXT = "&format=json&prop=wikitext&formatversion=2"

def call_html(search_term):
    """Returns response in HTML format"""

    resp = requests.get(f"{BASE_URL}{search_term}{FORMAT_PARAMETERS_HTML}").json()["parse"]["text"]
    import pdb; pdb.set_trace()

def call_wikitext(search_term):
    """Returns response in WikiText format"""

    resp = requests.get(f"{BASE_URL}{search_term}{FORMAT_PARAMETERS_WIKITEXT}").json()["parse"]["wikitext"]
    parse_for_sat(search_term)

def parse_for_sat(response, search_term):
    sat_count = response.count('atellite')
    if sat_count > 2:
        return response
    else:
        call_wikitext(f'{search_term}' + '_(Satellite)')
