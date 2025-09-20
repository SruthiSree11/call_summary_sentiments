# groq_client.py
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

MODEL = "llama-3.1-8b-instant"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_transcript(transcript: str):
    """
    Analyze transcript: summarize + extract sentiment.
    Always returns (summary, sentiment_str).
    Sentiment string is formatted as 'Polarity -> [Tone1, Tone2]'.
    """
    prompt = f"""
You are a customer service call transcript analysis assistant.

Analyze the following transcript and:
1. Summarize it in 2–3 sentences.
2. Provide sentiment analysis using this schema:
   {{
     "summary": "...",
     "sentiment": {{
       "overall_polarity": "Positive | Negative | Neutral | Mixed",
       "tones": ["tone1", "tone2", ...]
     }}
   }}

Guidelines:
- overall_polarity is one of: Positive, Negative, Neutral, Mixed.
- tones can be multiple, chosen from (case-insensitive):
  Frustrated, Angry, Annoyed, Disappointed, Confused, Impatient,
  Stressed/Anxious, Sarcastic, Skeptical/Distrustful, Indifferent/Apathetic,
  Helpless, Satisfied, Happy, Relieved, Grateful/Thankful, Excited,
  Calm, Informative, Questioning, Polite, Urgent.
- Use only tones from the list above.
- Do NOT add extra fields.

Transcript:
\"\"\"{transcript}\"\"\"

Respond ONLY in valid JSON.
"""


    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}  # enforce JSON
    )

    output = response.choices[0].message.content.strip()

    try:
        data = json.loads(output)
        summary = data["summary"]
        polarity = data["sentiment"]["overall_polarity"]
        tones = ", ".join(data["sentiment"]["tones"])
        sentiment = f"{polarity} -> [{tones}]"
        return summary, sentiment
    except (json.JSONDecodeError, KeyError) as e:
        return "Error in parsing response", str(e)
