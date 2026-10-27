import os
from google import genai
from google.genai import types

class StandardSynthesizer:
    def __init__(self):
        # Initializes client using environment variable GEMINI_API_KEY
        self.client = genai.Client()

    def analyze_standard(self, standard_data: dict) -> str:
        prompt = f"""
        Analyze the following ISO/IEC standard information and generate a structured study breakdown:
        
        Standard ID: {standard_data.get('standard_id')}
        Title: {standard_data.get('title')}
        Abstract: {standard_data.get('abstract')}
        
        Provide:
        1. Core objective and mandatory requirements.
        2. Key compliance clauses for software/system architecture.
        3. Potential failure modes or audit pitfalls.
        """
        
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                system_instruction="You are an expert Chief Compliance and Systems Architect specializing in ISO/IEC standards."
            )
        )
        return response.text
