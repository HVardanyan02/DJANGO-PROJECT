from django import forms
from .models import Job  
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'job_type', 'job_description']
        widgets = {
            'job_description': forms.Textarea(attrs={'class': 'editor'}), 
            'company_description': forms.Textarea(attrs={'class': 'editor'}), 
        }
