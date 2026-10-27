from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Expedition

def home (request) : 
    return HttpResponse("<h1>Welcome to ... </h1>")
def welcome (request , name) :
     return HttpResponse(f"hello {name} ")
def listExpeditions(request):
     liste = Expedition.objects.all()
     return render(request,'expedition/list.html',{"list":liste})
def detailExpedition(request, id):
     expedition = get_object_or_404(Expedition, id=id)
     return render(request, 'expedition/detail.html', {"expedition": expedition})