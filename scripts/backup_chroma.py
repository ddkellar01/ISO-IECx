"""Automated backup utility for ChromaDB vector database storage."""
import shutil
import os
from datetime import datetime

def backup_vector_store(data_dir: str = "./chroma_data", backup_dir: str = "./backups"):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"chroma_backup_{timestamp}")
    
    if os.path.exists(data_dir):
        shutil.copytree(data_dir, backup_path)
        print(f"Vector store successfully backed up to {backup_path}")
    else:
        print(f"Directory {data_dir} does not exist.")

if __name__ == "__main__":
    backup_vector_store()
