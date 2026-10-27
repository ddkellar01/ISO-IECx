"""Automated API health check script for monitoring production deployment."""
import sys
import requests

def check_health(url: str = "http://localhost:8080/health"):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Health check passed: {response.json()}")
            sys.exit(0)
        else:
            print(f"Health check failed with status code: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"Connection error during health check: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_health()
