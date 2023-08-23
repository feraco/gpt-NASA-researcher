from __future__ import annotations
import json
import requests

def search_arxiv(query: str, num_results: int = 4) -> str:
    base_url = "http://export.arxiv.org/api/query?"
    response = requests.get(base_url, params={"search_query": query, "max_results": num_results})
    # Parse the response as needed
    return response.text

def search_crossref(query: str, num_results: int = 4) -> str:
    base_url = "https://api.crossref.org/works?"
    response = requests.get(base_url, params={"query": query, "rows": num_results})
    return response.json()

def search_ntrs(query: str, num_results: int = 4) -> str:
    # Assuming NTRS provides an API endpoint (this is a placeholder)
    base_url = "https://ntrs.nasa.gov/api/search?"
    response = requests.get(base_url, params={"q": query, "rows": num_results})
    return response.json()

def search_openalex(query: str, num_results: int = 4) -> str:
    base_url = "https://api.openalex.org/search?"
    response = requests.get(base_url, params={"q": query, "rows": num_results})
    return response.json()

def web_search(query: str, database: str, num_results: int = 4) -> str:
    print(f"Searching {database} with query {query}...")
    if database == "arxiv":
        return search_arxiv(query, num_results)
    elif database == "crossref":
        return search_crossref(query, num_results)
    elif database == "ntrs":
        return search_ntrs(query, num_results)
    elif database == "openalex":
        return search_openalex(query, num_results)
    else:
        raise ValueError(f"Unknown database: {database}")

# Example usage
results = web_search("space exploration", "arxiv", 4)
print(results)
