"""Parses JTC 1 subcommittee technical documents and metadata."""
import requests
from bs4 import BeautifulSoup

class JTC1Parser:
    def __init__(self):
        self.base_url = "https://www.iso.org/committee/45020.html"

    def fetch_subcommittees(self) -> list:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(response.text, "html.parser")
        subcommittees = []
        for row in soup.select("table tbody tr"):
            cols = row.find_all("td")
            if len(cols) >= 2:
                subcommittees.append({
                    "sc_id": cols[0].get_text(strip=True),
                    "name": cols[1].get_text(strip=True)
                })
        return subcommittees
