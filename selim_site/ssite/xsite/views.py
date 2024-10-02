from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("homepages")

def blogs(request):
    return HttpResponse("blogs")

def blogs_details(request, id):
    return HttpResponse("blogs_details: "+ str(id))