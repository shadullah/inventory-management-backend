from django.shortcuts import render,HttpResponse

# Create your views here.
def products(req):
    return HttpResponse("hi i'm products page")