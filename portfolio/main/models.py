from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Skill(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="skills")
    score = models.IntegerField(default=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    bio = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = "Contact Profiles"
        verbose_name = "Contact Profile"
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self) -> str:
        return f"{self.name}"
