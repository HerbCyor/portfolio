from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import SkillSerializer
from main.models import Skill

# Create your views here.


@api_view(["GET"])
def apiOverView(request):

    api_urls = {
        "List": "/skill-list",
        "Detail View": "skill-detail/<str:pk>",
        "Create": "/skill-create",
        "Update": "/skill-update/<str:pk>",
        "Delete": "/skill-delete/<str:pk>",
    }

    return Response(api_urls)


@api_view(["GET"])
def skillList(request):

    skills = Skill.objects.all().order_by("id")
    serializer = SkillSerializer(skills, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def skillDetail(request, pk):
    skills = Skill.objects.get(id=pk)
    serializer = SkillSerializer(skills, many=False)
    return Response(serializer.data)


@login_required
@api_view(["POST"])
def skillCreate(request):

    serializer = SkillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@login_required
@api_view(["POST"])
def skillUpdate(request, pk):

    skill = Skill.objects.get(id=pk)
    serializer = SkillSerializer(instance=skill, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@login_required
@api_view(["DELETE"])
def SkillDelete(request, pk):
    skill = Skill.objects.get(id=pk)
    skill.delete()
    return Response("Skill succesfully deleted")
