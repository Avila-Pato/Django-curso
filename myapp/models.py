from django.db import models

# Create your models here. para la tabla de la base de datos
# ahi que conectarlo con settings.py en INSTALLED_APPS
class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(),
    # CASCADE: si se elimina un proyecto se eliminan todas las tareas
    project = models.ForeignKey(Project, on_delete=models.CASCADE)