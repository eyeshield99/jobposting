from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import JobPosting
from .forms import JobPostingForm

# Job Listing Views
class JobPostingListView(ListView):
    model = JobPosting
    template_name = 'job_board/job_listing.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']

class JobPostingDetailView(DetailView):
    model = JobPosting
    template_name = 'job_board/job_detail.html'
    context_object_name = 'job' 

def jobpost(request):
    form=JobPostingForm()

    if request.method=='POST':
        form=JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job-list')
    context={'form':form}
    return render(request,'job_board/job_form.html',context)

def deletejob(request, pk):
    obj=get_object_or_404(JobPosting,pk=pk)

    if request.method=='POST':
        obj.delete()
        return redirect('job-list')
    
    return render(request, 'job_board/confirmation_delete.html',{'job':obj})
    
def jobupdate(request, pk):
    obj = get_object_or_404(JobPosting, pk=pk)

    if request.method=='POST':
        form=JobPostingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('job-list')
    else:
        form =JobPostingForm(instance=obj)

    context={'form':form}
    return render(request,'job_board/job_form.html',context)     
    
    
