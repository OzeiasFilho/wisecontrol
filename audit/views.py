from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is the audit index.")