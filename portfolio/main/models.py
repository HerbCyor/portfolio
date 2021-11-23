from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Skill(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(
        blank=True, null=True, upload_to="skills", default="skills/default.png"
    )
    score = models.IntegerField(default=50, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
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


class Media(models.Model):
    class Meta:
        verbose_name_plural = "Media Files"
        verbose_name = "Media"
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
