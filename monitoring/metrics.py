"""Prometheus performance metrics exporter for ISO-IECx pipeline execution."""
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

REQUEST_COUNT = Counter("iso_iec_request_total", "Total API requests processed", ["endpoint", "method"])
LATENCY = Histogram("iso_iec_request_latency_seconds", "Request latency in seconds", ["endpoint"])

def metrics_endpoint():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
