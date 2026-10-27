"""Data schemas and Pydantic models for ISO/IEC standards and compliance audits."""
from pydantic import BaseModel
from typing import List, Optional

class StandardMetadata(BaseModel):
    standard_id: str
    title: str
    abstract: str
    source_url: str
    timestamp: float

class ComplianceFinding(BaseModel):
    control: str
    issue: str
    severity: str = "HIGH"

class AuditReport(BaseModel):
    standard_id: str
    compliant: bool
    total_issues: int
    findings: List[ComplianceFinding]
