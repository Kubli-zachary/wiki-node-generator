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
    G.add_node(root_title)
    for title in linked_titles:
        G.add_node(title)
        G.add_edge(root_title, title)
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
    summary["nodes"] = graph.number_of_nodes()
    summary["edges"] = graph.number_of_edges()
    summary["edge_list"] = list(graph.edges()) # nx.to_edgelist(graph) #
    print("Graph summary:", summary)
    return summary

def make_wiki_graph(root_url):
    html = fetch_html(root_url)
    links = extract_links(html)
    root_title = root_url.split("/")[-1].replace("_", " ")
    graph = build_graph(root_title, links)
    return format_graph_output(graph)

def make_deep_wiki_graph(root_url, depth=1):
    html = fetch_html(root_url)
    links = extract_links(html)
    root_title = root_url.split("/")[-1].replace("_", " ")
    graph = build_graph(root_title, links)
    
    for _ in range(depth):
        new_links = []
        for node in list(graph.nodes()):
            html = fetch_html(f"https://en.wikipedia.org/wiki/{node.replace(' ', '_')}")
            new_links += extract_links(html)
        new_links = list(set(new_links) - set(graph.nodes()))
        graph.add_nodes_from(new_links)
        for title in new_links:
            graph.add_edge(node, title)
    
    return format_graph_output(graph)

if __name__ == "__main__":
    root_url = "https://en.wikipedia.org/wiki/Computer_programming"
    print(make_wiki_graph(root_url))
    print(make_deep_wiki_graph(root_url, depth=2))