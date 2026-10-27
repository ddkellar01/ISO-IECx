"""Cleanup utility script to remove temporary cache files, build artifacts, and logs."""
import shutil
from pathlib import Path

def clean_workspace():
    root = Path(__file__).resolve().parent.parent
    patterns = ["**/__pycache__", "**/.pytest_cache", "build", "dist", "**/*.pyc"]
    
    for pattern in patterns:
        for path in root.glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"Removed directory: {path}")
            else:
                path.unlink()
                print(f"Removed file: {path}")
                
    print("Workspace successfully cleaned.")

if __name__ == "__main__":
    clean_workspace()
