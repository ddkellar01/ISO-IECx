"""Orchestrates Google Flow video generation execution and validates descriptions."""
from workflows.google_flow_video import GoogleFlowVideoGenerator

def run_batch_video_generation(standards_list: list):
    generator = GoogleFlowVideoGenerator(char_limit=350)
    batch_results = []
    
    for std_id in standards_list:
        summary = f"Full architectural compliance overview and threat evaluation for ISO/IEC {std_id}."
        result = generator.generate_flow_video(std_id, summary)
        batch_results.append(result)
        
    return batch_results

if __name__ == "__main__":
    test_standards = ["27001", "42001", "27017"]
    results = run_batch_video_generation(test_standards)
    print(f"Generated {len(results)} video prompts successfully.")
