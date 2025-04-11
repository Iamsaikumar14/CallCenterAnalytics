from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.holdtime_analyzer import HoldTimeAnalyzer
import tempfile
import shutil

router = APIRouter()
analyzer = HoldTimeAnalyzer()

@router.post("/holdtime")
async def get_hold_time(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            shutil.copyfileobj(file.file, tmp)
            temp_path = tmp.name

        result = analyzer.analyze_hold_time(temp_path)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
