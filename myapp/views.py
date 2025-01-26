from django.http import HttpResponse, JsonResponse
from.models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse("<h1> IndexPage</h1>")

def hello(request, username):
    return HttpResponse("<h1> Hello, %s </h1> " % username)

def about(request):
    return HttpResponse("<h1> About </h1>")

def projects(request):
    projects = Project.objects.all()
    return JsonResponse(list(projects.values()), safe=False)

def tasks(request, title):
    tasks =  get_object_or_404(Task, title=title)
    return HttpResponse("<h1> Tasks %s </h1>" % tasks.title)