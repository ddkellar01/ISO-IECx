"""Webhook event receiver for external compliance alerts and triggers."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class WebhookPayload(BaseModel):
    event_type: str
    source: str
    payload: dict

@router.post("/webhook/compliance-alert")
def handle_compliance_alert(alert: WebhookPayload):
    if not alert.event_type:
        raise HTTPException(status_code=400, detail="Missing event_type in payload.")
    
    print(f"Received webhook event [{alert.event_type}] from {alert.source}")
    return {"status": "received", "event": alert.event_type}
