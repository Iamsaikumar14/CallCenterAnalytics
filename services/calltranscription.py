import whisper
import os

class CallTranscriptionService:
    def __init__(self, model_size: str = "base"):
        self.model = whisper.load_model(model_size)

    def transcribe_audio(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            result = self.model.transcribe(file_path)
            return result.get("text", "")
        except Exception as e:
            raise RuntimeError(f"Transcription failed: {str(e)}")
