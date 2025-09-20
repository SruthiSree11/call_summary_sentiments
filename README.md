
```markdown
# Call Transcript Summary & Sentiment Analyzer

A Flask-based mini project that analyzes customer call transcripts using the **Groq API**.  
The app generates:
- A 2–3 sentence **summary** of the transcript  
- A detailed **sentiment classification** → overall polarity (Positive, Negative, Neutral, Mixed) and tone(s) (e.g., Angry, Frustrated, Polite, Grateful, etc.)  
- Saves results into `outputs/call_analysis.csv`  

---

## 🚀 Features
- Input transcript via simple web UI  
- Real-time summary + sentiment analysis  
- Structured JSON prompt ensures consistent output  
- Results stored in CSV for later review  

---

## 📂 Project Structure
```

call\_summary\_sentiment/
│── app.py              # Flask app
│── groq\_client.py      # API + analysis logic
│── requirements.txt    # Dependencies
│── outputs/
│    └── call\_analysis.csv
│── .env                # Contains GROQ\_API\_KEY

````

---

## ⚙️ Setup & Run
1. Clone repo & install dependencies:
   ```bash
   pip install -r requirements.txt
````

2. Add your **Groq API key** to `.env`:

   ```
   GROQ_API_KEY=your_key_here
   ```

3. Run Flask app:

   ```bash
   python app.py
   ```

4. Open browser at `http://127.0.0.1:5000`
   Paste a transcript → click **Analyze** → view summary & sentiment.

5. Check results in:

   ```
   outputs/call_analysis.csv
   ```

---

## 📝 Example

**Input Transcript:**

```
I love your product, but my last three deliveries were late and one was damaged.
```

**Output:**

* **Summary:** Customer praises product but reports repeated delivery issues.
* **Sentiment:** Mixed → \[Positive, Frustrated]

---

