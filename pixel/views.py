from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def home(request):
    posts=Image.show_images()
    return render(request,'home.html',{'posts':posts})

def search_category(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
