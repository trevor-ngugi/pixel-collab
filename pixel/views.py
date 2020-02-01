from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def home(request):
    posts=Image.show_images()
    return render(request,'home.html',{'posts':posts})
