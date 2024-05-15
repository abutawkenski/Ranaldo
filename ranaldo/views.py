from django.shortcuts import render
from .models import About, Resume, Experience, Skills, Skillss, Awards, Services,Project


# Create your views here.


def ranaldo(request):
    about = About.objects.all()
    resume = Resume.objects.all()
    experience = Experience.objects.all()
    skills = Skills.objects.all()
    skillss = Skillss.objects.all()
    awards = Awards.objects.all()
    services = Services.objects.all()
    project = Project.objects.all()


    ctx = {
        "about": about,
        "resume": resume,
        "experience": experience,
        "skills": skills,
        "skillss": skillss,
        "awards": awards,
        "services": services,
        "project": project,
    }

    return render(request, "index.html", ctx)
from django.shortcuts import render

# Create your views here.
