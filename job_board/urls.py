from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobPostingListView.as_view(), name='job-list'),
    path('job/<int:pk>/', views.JobPostingDetailView.as_view(), name='job-detail'),
    path('jobpost/', views.jobpost, name='job-post'),
    path('jobdelete/<int:pk>/', views.deletejob, name='job-delete'),
    path('jobupdate/<int:pk>/', views.jobupdate, name='job-update'),
    # Add more URL patterns for user profile, login, registration, etc.
]
