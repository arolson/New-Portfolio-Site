from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def projects(request):
    return render(request, 'portfolio_app/projects.html')

def about(request):
    return render(request, 'portfolio_app/about.html')
