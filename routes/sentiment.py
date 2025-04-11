from fastapi import APIRouter, HTTPException
from ..models.call import Utterance
from ..services.analysis import AnalysisService

router = APIRouter()
service = AnalysisService()

@router.post("/analyze")
def analyze_sentiment(utterances: list[Utterance]):
    try:
        timeline = service.analyze_utterances(utterances)
        return {
            "timeline": [entry.dict() for entry in timeline],
            "overall_sentiment": "analyzed"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
