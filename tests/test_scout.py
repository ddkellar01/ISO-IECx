"""Unit tests for the ISO-IECx crawler scout module."""
import pytest
from scouts.iso_crawler import ISOScout

def test_scout_initialization():
    scout = ISOScout()
    assert scout.headers is not None
    assert "User-Agent" in scout.headers

def test_scout_invalid_standard():
    scout = ISOScout()
    result = scout.scout_standard("99999999")
    assert "error" in result or result.get("title") == "N/A"
