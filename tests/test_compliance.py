"""Unit tests for the ISO-IECx compliance auditing module."""
import pytest
from evals.compliance_checker import ComplianceChecker

def test_compliant_config():
    checker = ComplianceChecker()
    valid_config = {
        "encryption_at_rest": True,
        "access_logging": True
    }
    report = checker.audit_config(valid_config)
    assert report["compliant"] is True
    assert report["total_issues"] == 0

def test_non_compliant_config():
    checker = ComplianceChecker()
    flawed_config = {
        "encryption_at_rest": False,
        "access_logging": False
    }
    report = checker.audit_config(flawed_config)
    assert report["compliant"] is False
    assert report["total_issues"] == 2
