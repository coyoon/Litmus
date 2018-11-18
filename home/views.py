from django.shortcuts import render

def index(request):
    context = {"nav_library": "active"}
    return render(request, 'library/color_list.html', context)
def home(request):
    context = {"nav_home": "active"}
    return render(request, 'home/home.html', context)
def library(request):
    context = {"nav_library": "active"}
    return render(request, 'library/color_list.html', context)
def about(request):
    context = {"nav_about": "active"}
    return render(request, 'home/about.html', context)