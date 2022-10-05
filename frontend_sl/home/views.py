from django.shortcuts import render

# Create your views here.

def index(request):
    user_slug = 'x'
    return render(request, 'home/index.html', {'user_slug': user_slug})