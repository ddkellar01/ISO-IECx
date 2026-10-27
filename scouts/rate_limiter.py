"""Token-bucket rate limiter to prevent IP blocking during scraping."""
import time

class RateLimiter:
    def __init__(self, delay_seconds: float = 2.0):
        self.delay = delay_seconds
        self.last_call = 0.0

    def wait(self):
        elapsed = time.time() - self.last_call
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self.last_call = time.time()
