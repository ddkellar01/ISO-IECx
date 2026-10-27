"""Celery worker tasks for asynchronous execution of scraping and AI jobs."""
import os
from celery import Celery
from scouts.iso_crawler import ISOScout
from learner.semantic_synthesizer import StandardSynthesizer

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
celery_app = Celery("iso_tasks", broker=redis_url, backend=redis_url)

@celery_app.task
def task_scout_and_study(standard_id: str):
    scout = ISOScout()
    data = scout.scout_standard(standard_id)
    synthesizer = StandardSynthesizer()
    analysis = synthesizer.analyze_standard(data)
    return {"standard_id": standard_id, "analysis_length": len(analysis)}
