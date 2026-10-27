import json
from pathlib import Path

class ComplianceChecker:
    def __init__(self, rules_path: str = None):
        if rules_path is None:
            root_dir = Path(__file__).resolve().parent.parent
            rules_path = root_dir / "config" / "standards_registry.json"
            
        with open(rules_path, "r") as f:
            self.registry = json.load(f)

    def audit_config(self, config_dict: dict) -> dict:
        findings = []
        if not config_dict.get("encryption_at_rest", False):
            findings.append({"control": "ISO/IEC 27001", "issue": "Missing encryption at rest"})
        if not config_dict.get("access_logging", False):
            findings.append({"control": "ISO/IEC 27002", "issue": "Access logging disabled"})
            
        return {
            "compliant": len(findings) == 0,
            "total_issues": len(findings),
            "findings": findings
        }
