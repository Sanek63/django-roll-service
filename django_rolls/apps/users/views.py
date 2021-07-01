from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lk(request):
    return HttpResponse("<h1>Priv</h1>")
