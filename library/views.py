from django.shortcuts import render

def color_list(request):
    return render(request, 'library/color_list.html', {})
