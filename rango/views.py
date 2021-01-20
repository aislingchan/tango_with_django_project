from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""Rango says hey there partner!
<a href=http://127.0.0.1:8000/rango/about/>About?<a>""")

def about(request):
    return HttpResponse("""Rango says here is the about page.
<a href=http://127.0.0.1:8000/rango/>Index!<a>""")
