from pydub import AudioSegment, silence
import os

class HoldTimeAnalyzer:
    def __init__(self, silence_thresh: int = -40, min_silence_len: int = 2000):
        self.silence_thresh = silence_thresh
        self.min_silence_len = min_silence_len

    def analyze_hold_time(self, file_path: str) -> dict:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        audio = AudioSegment.from_file(file_path, format="mp3")
        duration_sec = len(audio) / 1000

        silent_ranges = silence.detect_silence(
            audio,
            min_silence_len=self.min_silence_len,
            silence_thresh=self.silence_thresh
        )

        hold_times = [(start/1000, end/1000) for start, end in silent_ranges]
        total_silence_sec = sum((end - start) for start, end in silent_ranges) / 1000

        return {
            "duration": duration_sec,
            "total_silence": total_silence_sec,
            "silent_segments": [
                {
                    "start": round(start, 2),
                    "end": round(end, 2),
                    "duration": round(end - start, 2)
                }
                for start, end in hold_times
            ]
        }
