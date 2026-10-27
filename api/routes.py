"""API route handlers for scouting, analysis, and Google Flow video generation."""
from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from scouts.iso_crawler import ISOScout
from learner.semantic_synthesizer import StandardSynthesizer
from workflows.google_flow_video import GoogleFlowVideoGenerator

router = APIRouter()

class IngestRequest(BaseModel):
    standard_id: str

class VideoPromptRequest(BaseModel):
    standard_id: str
    summary: str

@router.post("/scout")
def trigger_scout(req: IngestRequest):
    scout = ISOScout()
    data = scout.scout_standard(req.standard_id)
    if "error" in data:
        raise HTTPException(status_code=404, detail=data["error"])
    return data

@router.post("/synthesize")
def trigger_synthesis(req: IngestRequest):
    scout = ISOScout()
    data = scout.scout_standard(req.standard_id)
    synthesizer = StandardSynthesizer()
    analysis = synthesizer.analyze_standard(data)
    return {"standard_id": req.standard_id, "analysis": analysis}

@router.post("/generate-video-prompt")
def generate_video_prompt(req: VideoPromptRequest):
    generator = GoogleFlowVideoGenerator(char_limit=350)
    prompt = generator.format_video_description(req.standard_id, req.summary)
    return {"standard_id": req.standard_id, "prompt": prompt, "character_count": len(prompt)}
