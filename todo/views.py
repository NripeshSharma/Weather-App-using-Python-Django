from django.shortcuts import render
import requests

# Create your views here.
def todo(request):
    return render(request, 'ToDo.html')