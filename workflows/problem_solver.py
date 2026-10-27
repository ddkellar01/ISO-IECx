"""Autonomous agent that suggests resolution steps for compliance violations."""
from google import genai

class ProblemSolverAgent:
    def __init__(self):
        self.client = genai.Client()

    def solve_violation(self, violation_description: str) -> str:
        prompt = f"Provide actionable code or configuration fixes for this compliance violation: {violation_description}"
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
