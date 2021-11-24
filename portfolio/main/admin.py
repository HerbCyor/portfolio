from django.contrib import admin
from .models import Skill, UserProfile, ContactProfile, Media
import csv
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

# Register your models here.


@admin.action(description="Export as csv")
def export_as_csv(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type="text/csv")
    # force download.
    response["Content-Disposition"] = "attachment;filename=export.csv"
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    actions = [export_as_csv]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "name")
