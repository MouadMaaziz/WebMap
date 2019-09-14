from django.shortcuts import render
from django.http import HttpResponse
from .models import Etablissements

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    #return HttpResponse("hello Grey")
    return render(request,"home.html" ,{})

def webmap_view(request,*args,**kwargs):
    #return HttpResponse("hello Grey")

    return render(request,"webmap.html" ,{})

def base_view(request,*args,**kwargs):
    #return HttpResponse("hello Grey")
    return render(request,"base.html" ,{})
