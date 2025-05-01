# AI_Resume-Exctraction-with-HR-chat-bot

This project uses a Large Language Model (LLM) to extract structured information from uploaded PDF resumes and enables an HR assistant chatbot to query candidate data — helping recruiters find the best talent faster.

---

## 🚀 Features

✅ Upload and process resumes in PDF format  
✅ Extract structured fields using Gemini LLM (not regex!)  
✅ Extracts:
- First Name
- Last Name
- Email Address
- Phone Number
- Education History
- Work Experience Summary
- Skills
- Current Position
- Years of Experience

✅ Built-in HR Chatbot API to ask:
- “Who is best at Python?”
- “Rank candidates for an AI role.”

---

## 🛠 Tech Stack

- **Python**
- **Flask** (API + minimal UI)
- **Gemini API (Google Generative AI)**
- **PyPDF2** for reading PDF content

---

## 🧑‍💻 Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/Mighty2Skiddie/AI_Resume-Extraction-with-HR-chat-bot.git
cd llm-resume-parser
```

### 2. Install dependencies
```bash
pip install flask PyPDF2 google-generativeai
```

### 3. Set your Gemini API Key
In `app.py`, update this line:
```python
os.environ["GOOGLE_API_KEY"] = "your-gemini-api-key"
```

---

## ▶️ How to Run

```bash
python app.py
```

Then visit:
```
http://127.0.0.1:5000/
```

Upload a `.pdf` resume and see the extracted structured information.

---

## 💬 HR Chatbot (POST API)

Endpoint:
```
POST /hr_query
```

Sample body:
```json
{
  "question": "Who is the most skilled in Python?"
}
```

Returns:
```json
{
  "answer": "Ashish Chaturvedi has strong Python and AI experience and would be the best fit."
}
```

---

## 📂 Project Structure

```
├── app.py               # Flask backend
├── index.html           # Resume upload form
├── templates/           # HTML templates (Flask expects this folder)
├── README.md            # You’re here
```

---

## 📸 Screenshots / Demo Video

📌 Include a Loom/Youtube link or GIF showing resume upload + chatbot working here.

---

## 📌 Assumptions & Notes

- Only accepts `.pdf` resumes
- Assumes resumes have extractable (non-image) text
- Gemini API must be valid and active
- Data is stored in memory (no DB)

---

## 💡 Future Improvements

- Add vector DB for semantic search
- Add login system for HR users
- Store resumes in cloud + add user feedback loop
- Add ranking model based on job description

---

## 🧠 License

MIT License — feel free to use and modify.
```
