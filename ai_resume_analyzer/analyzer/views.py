# analyzer/views.py
from django.shortcuts import render
from .models import Resume
from .forms import ResumeUploadForm
from .utils import extract_text, analyze_resume

def upload_resume(request):
    """
    Handles resume upload, extracts text, and analyzes it with AI.
    """
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()

            file = resume.resume_file
            text = extract_text(file)

            if "Error" in text or text.strip() == "":
                return render(request, "upload.html", {"form": form, "error": "Failed to extract text from file."})

            result = analyze_resume(text)

            if "Error" in result:
                return render(request, "upload.html", {"form": form, "error": "AI analysis failed."})

            return render(request, "result.html", {"result": result})

    else:
        form = ResumeUploadForm()

    return render(request, "upload.html", {"form": form})