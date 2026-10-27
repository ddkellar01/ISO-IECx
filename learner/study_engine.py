"""Generates interactive flashcards and study modules for ISO/IEC certs."""
from google import genai
from google.genai import types

class StudyEngine:
    def __init__(self):
        self.client = genai.Client()

    def build_flashcards(self, standard_id: str, abstract: str) -> str:
        prompt = f"Create 5 flashcards (Question/Answer) for ISO/IEC {standard_id} based on: {abstract}"
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.3)
        )
        return response.text
