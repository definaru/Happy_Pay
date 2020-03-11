from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template import RequestContext


def index(request):
    return TemplateResponse(request,  "store/home.html")
    
def about(request):
    return TemplateResponse(request,  "store/about.html")
    
def contact(request):
    return HttpResponse("Контакты")   
    
def signup(request):
    return TemplateResponse(request, "dachboard/signup.html")    

def login(request):
    return TemplateResponse(request, "dachboard/login.html")
    
def handler403(request):
    return render(request, "error/403.html") 
    
def handler404(request):
    return render(request, "error/404.html")  
    
def handler500(request):
    return render(request, "error/500.html")
    
    
    