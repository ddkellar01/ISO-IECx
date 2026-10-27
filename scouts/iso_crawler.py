import requests
from bs4 import BeautifulSoup
import json
import time
from pathlib import Path

class ISOScout:
    def __init__(self, registry_path: str = None):
        if registry_path is None:
            # Resolve path relative to project root
            root_dir = Path(__file__).resolve().parent.parent
            registry_path = root_dir / "config" / "standards_registry.json"
            
        with open(registry_path, "r") as f:
            self.registry = json.load(f)
        self.headers = {"User-Agent": "ISO-IECx-ScoutBot/1.0 (Research Automation)"}

    def scout_standard(self, standard_id: str):
        url = f"https://www.iso.org/standard/{standard_id}.html"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                return {"error": f"Failed to fetch {standard_id}", "status": response.status_code}
                
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("h1", class_="title")
            abstract = soup.find("div", id="abstract")
            
            return {
                "standard_id": standard_id,
                "title": title.get_text(strip=True) if title else "N/A",
                "abstract": abstract.get_text(strip=True) if abstract else "N/A",
                "source_url": url,
                "timestamp": time.time()
            }
        except Exception as e:
            return {"error": str(e), "standard_id": standard_id}

    def run_sweep(self):
        results = []
        for std in self.registry.get("target_ids", []):
            results.append(self.scout_standard(std))
            time.sleep(1.5)
        return results
