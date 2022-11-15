from django.shortcuts import render
from .models import Project

def index_view(request):
    # projects = Project.objects.all()
    projects = Project.objects.filter(pk__lt=4)
    return render(request, "portfolio/index.html", {"title":"Главная страница", "projects": projects})
