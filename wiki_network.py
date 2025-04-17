import requests
from bs4 import BeautifulSoup

# Get the HTML from a Wikipedia article
def fetch_html(url):
    html = ""
    # TODO: Use requests to fetch the page content
    print("Fetched HTML")
    return html

# Extract internal article links from the HTML
def extract_links(html, max_links=10):
    links = []
    # TODO: Use BeautifulSoup to find valid /wiki/ links without colons
    print("Extracted links:", links)
    return links