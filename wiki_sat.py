"""Makes a call using sat name and returns the wiki page content"""

from flask import Flask
import requests

BASE_URL = "https://en.wikipedia.org/w/api.php?action=parse&page="

Magnum_(satellite)

FORMAT_PARAMETERS = "&format=json&prop=wikitext&formatversion=2"

def call_wiki(search_term):
    resp = requests.get(f"{BASE_URL}{search_term}{FORMAT_PARAMETERS}").json()
    import pdb; pdb.set_trace()