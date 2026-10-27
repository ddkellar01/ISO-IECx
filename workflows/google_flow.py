from fastapi import FastAPI, BackgroundTasks
from scouts.iso_crawler import ISOScout
from learner.semantic_synthesizer import StandardSynthesizer
from workflows.google_flow_video import GoogleFlowVideoGenerator
from pydantic import BaseModel

app = FastAPI(title="ISO-IECx Google Flow Engine with Video Generation")

class StandardRequest(BaseModel):
    standard_id: str

@app.post("/ingest-study-and-visualize")
def ingest_study_and_visualize(req: StandardRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_full_pipeline, req.standard_id)
    return {"status": "Queued with Video Pipeline", "standard_id": req.standard_id}

def process_full_pipeline(standard_id: str):
    # 1. Scout and pull standard
    scout = ISOScout()
    data = scout.scout_standard(standard_id)
    
    # 2. Learn / Synthesize via Gemini
    synthesizer = StandardSynthesizer()
    analysis = synthesizer.analyze_standard(data)
    
    # 3. Generate Google Flow Video with 350-character description constraint
    video_gen = GoogleFlowVideoGenerator(char_limit=350)
    video_result = video_gen.generate_flow_video(standard_id, analysis)
    
    print(f"Pipeline complete for {standard_id}. Video prompt generated successfully.")
