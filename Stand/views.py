from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Homepage under construction.")

def open(request):
    return HttpResponse("Simulator here...")

def close(request):
    return HttpResponse("Game Over screen here...")
