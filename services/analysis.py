from transformers import pipeline
from ..models.call import Utterance, SentimentAnalysis

class AnalysisService:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def analyze_utterances(self, utterances: list[Utterance]) -> list[SentimentAnalysis]:
        results = []
        texts = [u.text for u in utterances]
        sentiments = self.sentiment_pipeline(texts)

        for i, utterance in enumerate(utterances):
            sentiment = sentiments[i]
            score = sentiment["score"]
            label = sentiment["label"]

            # Normalize value for timeline (e.g., negative=0, positive=1)
            if label.lower() == "negative":
                value = 0.0
            elif label.lower() == "neutral":
                value = 0.5
            else:
                value = 1.0

            results.append(SentimentAnalysis(
                time=utterance.timestamp,
                value=value,
                speaker=utterance.speaker,
                label=label
            ))

        return results

