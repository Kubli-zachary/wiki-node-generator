import requests
from bs4 import BeautifulSoup

# WIKI FETCH AND LINK EXTRACTION

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

# GRAPH CREATION
import networkx as nx

# Build a directed graph from a root node and its outgoing links
def build_graph(root_title, linked_titles):
    G = nx.DiGraph()
    # TODO: Add root node and edges from root to each linked title
    print("Graph nodes:", G.nodes())
    print("Graph edges:", G.edges())
    return G

# Print graph summary and return a simple object
def format_graph_output(graph):
    summary = {
        "nodes": 0,
        "edges": 0,
        "edge_list": []
    }
    # TODO: Fill in node count, edge count, and list of edges
    print("Graph summary:", summary)
    return summary

def make_wiki_graph(root_url):
    html = fetch_html(root_url)
    links = extract_links(html)
    root_title = root_url.split("/")[-1].replace("_", " ")
    graph = build_graph(root_title, links)
    return format_graph_output(graph)