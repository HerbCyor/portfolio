from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverView, name="api-overview"),
    path("skill-list/", views.skillList, name="skill-list"),
    path("skill-detail/<str:pk>", views.skillDetail, name="task-detail"),
    path("skill-create/", views.skillCreate, name="skill-create"),
    path("skill-update/<str:pk>", views.skillUpdate, name="skill-update"),
    path("skill-delete/<str:pk>", views.SkillDelete, name="skill-delete"),
    path("api", views.apiHome, name="apihome"),
]
