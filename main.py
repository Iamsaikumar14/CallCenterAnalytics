from fastapi import FastAPI
from routes import sentiment , transcription

app = FastAPI(
    title="Call Center Analytics API",
    description="Analyze agent-customer conversations using sentiment analysis.",
    version="1.0"
)

app.include_router(sentiment.router, prefix="/sentiment")
app.include_router(transcription.router, prefix="/transcription")
