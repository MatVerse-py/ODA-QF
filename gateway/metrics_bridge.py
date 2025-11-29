import requests

def fetch_remote_metrics(url: str):
    r = requests.get(url, timeout=3)
    return r.json()
