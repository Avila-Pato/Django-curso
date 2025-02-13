from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="Descripcion de tarea", widget=forms.Textarea)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo de projecto", max_length=200)
