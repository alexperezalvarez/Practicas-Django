from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hola me encuentro en la aplicacion home.")

def home(request):
    return HttpResponse("<h2>Hola me encuentro en la aplicacion Home.")



