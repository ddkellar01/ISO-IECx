"""Database and collection seeder for initializing standard registries."""
import json
from scouts.iso_crawler import ISOScout
from learner.semantic_synthesizer import StandardSynthesizer
from knowledge_base.vector_store import VectorStore

def seed_database(registry_path: str = "config/standards_registry.json"):
    with open(registry_path, "r") as f:
        data = json.load(f)
        
    scout = ISOScout()
    synthesizer = StandardSynthesizer()
    vector_store = VectorStore()
    
    for std_id in data.get("target_ids", []):
        print(f"Seeding standard ISO/IEC {std_id}...")
        std_data = scout.scout_standard(std_id)
        if "error" not in std_data:
            analysis = synthesizer.analyze_standard(std_data)
            vector_store.upsert_standard(std_id, std_data, analysis)
            print(f"Successfully seeded ISO/IEC {std_id}")

if __name__ == "__main__":
    seed_database()
