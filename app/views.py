from django.shortcuts import render

# Create your views here.
def ram(request):
    return render(request,'ram.html')
def sita(request):
    return render(request,'sita.html')
def hanuman(request):
    return render(request,'hanuman.html')
def lakshman(request):
    return render(request,'lakshman.html')
def garuda(request):
    return render(request,'garuda.html')