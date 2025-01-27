from django.http import HttpResponse

from myapp.forms import CreateNewProject, CreateNewTask
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    title = "Welcome to Django course"
    return render(request, "index.html", {"title": title})


def about(request):
    username = "pato"
    return render(request, "about.html", {"username": username})


def hello(request, username):
    return HttpResponse("<h1> Hello, %s </h1> " % username)


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})


def tasks(
    request,
):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_tasks(request):
    # Crear una tarea
    if request.method == "GET":
        return render(request, "tasks/create_tasks.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("/tasks/")


def create_projects(request):
    if request.method == "GET":
        return render(
            # muestra el formulario para crear un proyecto
            request,
            "projects/create_projects.html",
            {"form": CreateNewProject()},
        )
        # crea un proyecto y redirige a la lista de proyectos
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect("/projects/")
