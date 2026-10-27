"""Builds cross-reference graph maps between ISO/IEC standards."""
import json

class StandardGraphBuilder:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_standard(self, standard_id: str, title: str, domain: str):
        self.nodes[standard_id] = {"title": title, "domain": domain}

    def add_reference(self, source_id: str, target_id: str, relationship: str):
        self.edges.append({
            "source": source_id,
            "target": target_id,
            "relationship": relationship
        })

    def export_graph(self, filepath: str = "knowledge_base/graph.json"):
        with open(filepath, "w") as f:
            json.dump({"nodes": self.nodes, "edges": self.edges}, f, indent=2)
