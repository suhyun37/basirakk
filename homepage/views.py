from django.shortcuts import render

def index(request):
    return render(request, "homepage/index.html")
    
def about(request):
    return render(request, "about.html")
    
def post(request):
    return render(request, "post.html")

# Create your views here.
