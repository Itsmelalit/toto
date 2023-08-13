from django.shortcuts import render
from . import urls
# Create your views here.
def home(request):
    return render(request,'home.html')