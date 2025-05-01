from flask import Flask, render_template, request, jsonify
from PyPDF2 import PdfReader
import google.generativeai as genai
import os
import json

# Set your Google Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBAOZdYCq2uoHKXoZ0iFAh1bqCIBSLoJxw"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = Flask(__name__)
model = genai.GenerativeModel("models/gemini-1.5-pro")

# In-memory storage for parsed candidate data
parsed_resumes = []

def resumes_details(resume):
    prompt = f"""
You are an expert resume parser. From the resume text below, extract the following fields:

- First Name
- Last Name
- Email Address
- Phone Number
- Education History
- Work Experience Summary
- Skills
- Current Position
- Years of Experience

Resume:
{resume}

Return the result in JSON format like:
{{
  "First Name": "",
  "Last Name": "",
  "Email Address": "",
  "Phone Number": "",
  "Education History": [ ... ],
  "Work Experience Summary": "...",
  "Skills": [ ... ],
  "Current Position": "",
  "Years of Experience": ""
}}
"""
    response = model.generate_content(prompt).text
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "Empty filename"})

    text = ""
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()

    response = resumes_details(text)
    response_clean = response.replace("```json", "").replace("```", "").strip()
    data = json.loads(response_clean)

    first_name = data.get("First Name", "")
    last_name = data.get("Last Name", "")
    email = data.get("Email Address", "")
    phone = data.get("Phone Number", "")
    education = data.get("Education History", [])
    work_summary = data.get("Work Experience Summary", "")
    skills = ", ".join(data.get("Skills", []))
    position = data.get("Current Position", "")
    experience_years = data.get("Years of Experience", "")

    parsed_resumes.append({
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email,
        "Phone": phone,
        "Education History": education,
        "Work Experience Summary": work_summary,
        "Skills": skills,
        "Current Position": position,
        "Years of Experience": experience_years
    })

    return render_template("index.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        education=education,
        work_summary=work_summary,
        skills=skills,
        position=position,
        experience_years=experience_years
    )

@app.route("/hr_query", methods=["POST"])
def hr_query():
    question = request.json.get("question")
    all_profiles = json.dumps(parsed_resumes, indent=2)
    prompt = f"""
You are an HR assistant helping to find the best candidates.

Here are the candidate profiles:
{all_profiles}

Answer this question:
{question}
"""
    response = model.generate_content(prompt).text
    return jsonify({"answer": response.strip()})

if __name__ == "__main__":
    app.run(debug=True)