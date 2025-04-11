from pydantic import BaseModel
# from typing import List, Optional

class Utterance(BaseModel):
    speaker: str  # e.g., "agent" or "customer"
    text: str
    timestamp: float  # in seconds

class SentimentAnalysis(BaseModel):
    time: float
    value: float
    speaker: str
    label: str
