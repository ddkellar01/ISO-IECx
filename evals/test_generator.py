"""Generates automated compliance test cases based on ISO/IEC clauses."""
from google import genai
from google.genai import types

class ComplianceTestGenerator:
    def __init__(self):
        self.client = genai.Client()

    def generate_pytest(self, standard_id: str, clause_summary: str) -> str:
        prompt = f"Generate PyTest code validating compliance for ISO/IEC {standard_id}: {clause_summary}"
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a QA automation engineer writing clean PyTest scripts."
            )
        )
        return response.text
