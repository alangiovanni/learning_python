from django.shortcuts import render

# Create your views here.

def index(request):
    """Initial Page of Pizzaria"""
    return render(request, 'pizza/index.html')
