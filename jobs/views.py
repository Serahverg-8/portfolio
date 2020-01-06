from django.shortcuts import render

from .models import Job

# we see that a major portion of the jobs objeccts are in the home page.So we create the home page here
# Create your views here.
# say there are two home pages to avoid confusion we create jobs inside templates

def home_view(request):
    Jobs=Job.objects.all()
    return render(request,'jobs/home.html',{"jobs":Jobs})