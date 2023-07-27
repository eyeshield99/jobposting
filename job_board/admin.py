from django.contrib import admin
from . import models
# Register your models here.
myModels = [models.Employer, models.Employee, models.JobPosting]  # iterable list
admin.site.register(myModels)
