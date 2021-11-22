from django.shortcuts import render

from .forms import ContactForm
from .models import Skill, UserProfile

# Create your views here.
def Index(request):

    skills = list(Skill.objects.filter(is_active=True))
    profile = UserProfile.objects.all()
    context = {"skills": skills, "profile": profile}

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # create a form submitted message
    return render(request, "main/index.html", context)
