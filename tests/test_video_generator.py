"""Unit tests verifying the 350-character limit enforcement for Google Flow video prompts."""
import pytest
from workflows.google_flow_video import GoogleFlowVideoGenerator

def test_video_prompt_length_constraint():
    generator = GoogleFlowVideoGenerator(char_limit=350)
    long_summary = "A" * 500  # Extremely long summary text
    prompt = generator.format_video_description("27001", long_summary)
    
    assert len(prompt) <= 350
    assert prompt.endswith("...")

def test_normal_video_prompt():
    generator = GoogleFlowVideoGenerator(char_limit=350)
    prompt = generator.format_video_description("42001", "AI management system audit.")
    assert len(prompt) <= 350
    assert "42001" in prompt
