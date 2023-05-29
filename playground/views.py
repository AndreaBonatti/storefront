from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# view = request handler

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Andrea'})