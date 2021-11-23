from django.shortcuts import render

from .forms import ContactForm
from .models import Skill, UserProfile

from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def Index(request):

    skills = list(Skill.objects.filter(is_active=True))
    profile = UserProfile.objects.all()[0]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you for your message. I will be in contact soon"
            )

            # create a form submitted message
    else:
        form = ContactForm()

    context = {"skills": skills, "profile": profile, "form": form}

    return render(request, "main/index.html", context)
