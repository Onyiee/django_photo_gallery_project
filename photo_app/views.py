from django.shortcuts import render
from .models import Image


# Create your views here.

def home_page(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, "index.html", context)
