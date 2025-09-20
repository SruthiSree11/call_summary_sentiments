import os
import pandas as pd
from flask import Flask, render_template, request
from groq_client import analyze_transcript

app = Flask(__name__)

CSV_PATH = os.path.join("outputs", "call_analysis.csv")
os.makedirs("outputs", exist_ok=True)

def save_to_csv(transcript, summary, sentiment, filename=CSV_PATH):
    df = pd.DataFrame([[transcript, summary, sentiment]],
                      columns=["Transcript", "Summary", "Sentiment"])
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        transcript = request.form["transcript"]
        summary, sentiment = analyze_transcript(transcript)

        save_to_csv(transcript, summary, sentiment)

        return render_template(
            "index.html",
            transcript=transcript,
            summary=summary,
            sentiment=sentiment,
            saved=True
        )

    return render_template("index.html", saved=False)

if __name__ == "__main__":
    app.run(debug=True)
