"""
Google Flow Video Generator Integration for ISO-IECx
Generates compliant video walkthroughs and summaries from ISO/IEC analysis.
Constraint: All prompt descriptions must be strictly <= 350 characters.
"""

class GoogleFlowVideoGenerator:
    def __init__(self, char_limit: int = 350):
        self.char_limit = char_limit

    def format_video_description(self, standard_id: str, analysis_summary: str) -> str:
        """
        Creates a concise video generation description strictly capped at 350 characters.
        """
        raw_prompt = f"ISO/IEC {standard_id} compliance walkthrough and system security overview: {analysis_summary}"
        
        if len(raw_prompt) > self.char_limit:
            # Truncate cleanly to fit within the 350-character limit
            return raw_prompt[:self.char_limit - 3] + "..."
        return raw_prompt

    def generate_flow_video(self, standard_id: str, analysis_summary: str):
        prompt = self.format_video_description(standard_id, analysis_summary)
        
        # Enforce strict 350-character validation
        if len(prompt) > self.char_limit:
            raise ValueError(f"Prompt length ({len(prompt)}) exceeds the 350-character limit.")
            
        print(f"[Google Flow] Generating video with prompt ({len(prompt)} chars):\n{prompt}")
        
        # Return payload ready for video generation orchestration
        return {
            "status": "success",
            "standard_id": standard_id,
            "video_prompt": prompt,
            "character_count": len(prompt)
        }
