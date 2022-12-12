from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def projects(request):
    name = "andrew"
    return render(request, 'portfolio_app/projects.html')

def about(request):
    return render(request, 'portfolio_app/about.html')

def custom_404(request, exception):
    return render(request, 'portfolio_app/404.html', {}, status=404)
