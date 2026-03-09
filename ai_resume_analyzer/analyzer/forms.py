# analyzer/forms.py
from django import forms
from .models import Resume

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_file']
        widgets = {
            'resume_file': forms.ClearableFileInput(attrs={'class': 'file-input'})
        }