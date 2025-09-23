
#  Call Transcript Summary & Sentiment Analyzer

A **Flask-based mini project** that analyzes customer call transcripts using the **Groq API**.  

The app automatically:  
- Summarizes the conversation in **2–3 sentences**  
- Extracts detailed **sentiment** → overall polarity *(Positive / Negative / Neutral / Mixed)* and tone(s) *(e.g., Angry, Frustrated, Polite, Grateful, etc.)*  
- Saves results into a CSV file for review  

---

##  Features
- Simple **web UI** for entering transcripts  
- Real-time **summary + sentiment analysis**  
- Structured JSON ensures **consistent output**  
- Automatic CSV logging in `outputs/call_analysis.csv`  

---

##  Project Structure
```text
call_summary_sentiment/
├── app.py              # Flask app
├── groq_client.py      # Groq API + analysis logic
├── requirements.txt    # Dependencies
├── outputs/            # Folder to store results
│   └── call_analysis.csv
└── .env                # Contains GROQ_API_KEY
````

---

##  Setup & Run

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your Groq API key** in `.env`:

   ```ini
   GROQ_API_KEY=your_key_here
   ```

3. **Run Flask app**

   ```bash
   python app.py
   ```

4. Open browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)

   * Paste transcript
   * Click **Analyze**
   * View summary + sentiment

5. **Check results** in:

   ```text
   outputs/call_analysis.csv
   ```

---

##  Example

**Input Transcript:**

```text
I love your product, but my last three deliveries were late and one was damaged.
```

**Output:**

```text
Summary: Customer praises product but reports repeated delivery issues.  
Sentiment: Mixed → [Positive, Frustrated]
```

---

##  Notes

* Keep `.env` private (never commit your API key).
* This is a demo project — can be extended for dashboards or real call center integration.

---



