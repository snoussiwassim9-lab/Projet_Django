from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Expedition

def home (request) : 
    return HttpResponse("<h1>Welcome to ... </h1>")
def welcome (request , name) :
     return HttpResponse(f"hello {name} ")
def listExpeditions(request):
     liste = Expedition.objects.filter(statut='p')
     return render(request,'expedition/list.html',{"list":liste})
def detailExpedition(request, id):
     expedition = Expedition.objects.get(id=id)
     return render(request, 'expedition/detail.html', {"expedition": expedition})
def deleteExpedition(request, id):
     expedition = get_object_or_404(Expedition, id=id)
     if request.method == 'POST':
          expedition.delete()
          return redirect('list')
     return render(request, 'expedition/delete.html', {"expedition": expedition})