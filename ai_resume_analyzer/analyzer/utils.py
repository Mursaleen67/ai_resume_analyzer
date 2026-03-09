# analyzer/utils.py
import PyPDF2
import docx
import ollama

def extract_text(file):
    text = ""

    if file.name.endswith(".pdf"):
        try:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            if not text.strip():
                return "No extractable text found in PDF."
        except Exception as e:
            return f"Error reading PDF: {e}"

    elif file.name.endswith(".docx"):
        try:
            doc = docx.Document(file)
            for para in doc.paragraphs:
                text += para.text + "\n"
            if not text.strip():
                return "No extractable text found in DOCX."
        except Exception as e:
            return f"Error reading DOCX: {e}"
    else:
        return "Unsupported file format. Please upload PDF or DOCX."

    return text


def analyze_resume(resume_text):
    if not resume_text.strip():
        return "No text to analyze."

    prompt = f"""
    Analyze this resume and return a structured response:

    1. Resume score out of 100
    2. Skills found
    3. Missing skills
    4. Suggestions for improvement

    Resume:
    {resume_text}
    """

    try:
        response = ollama.chat(
            model="phi3",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error analyzing resume: {e}"