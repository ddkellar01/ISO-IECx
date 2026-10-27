"""Automated bulk ingestion script for core ISO/IEC standards catalogs."""
import time
from scouts.iso_crawler import ISOScout
from learner.semantic_synthesizer import StandardSynthesizer
from scouts.rate_limiter import RateLimiter

CORE_STANDARDS = ["27001", "27002", "27017", "27018", "42001", "22989", "25010", "15288", "30141", "20000"]

def run_bulk_ingestion():
    scout = ISOScout()
    synthesizer = StandardSynthesizer()
    limiter = RateLimiter(delay_seconds=2.0)
    
    print(f"Starting bulk ingestion for {len(CORE_STANDARDS)} core ISO/IEC standards...")
    for std_id in CORE_STANDARDS:
        limiter.wait()
        print(f"Fetching standard ISO/IEC {std_id}...")
        data = scout.scout_standard(std_id)
        if "error" not in data:
            analysis = synthesizer.analyze_standard(data)
            print(f"Successfully processed ISO/IEC {std_id} (Analysis length: {len(analysis)} chars)")
        else:
            print(f"Failed to fetch ISO/IEC {std_id}")

if __name__ == "__main__":
    run_bulk_ingestion()
