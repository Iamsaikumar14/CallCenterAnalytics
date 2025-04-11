from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.calltranscription import CallTranscriptionService
import tempfile
import shutil

router = APIRouter()
transcription_service = CallTranscriptionService()

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        transcription = transcription_service.transcribe_audio(tmp_path)
        return {"transcription": transcription}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
