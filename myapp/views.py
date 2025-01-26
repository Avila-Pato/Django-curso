from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> IndexPage</h1>")

def hello(request, username):
    return HttpResponse("<h1> Hello, World! </h1>")

def about(request):
    return HttpResponse("<h1> About </h1>")