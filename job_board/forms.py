from django.forms import ModelForm
from . models import JobPosting,Employee,Employer

class JobPostingForm(ModelForm):
    class Meta:
        model = JobPosting
        fields = "__all__"
