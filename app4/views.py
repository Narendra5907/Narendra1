from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app4(request):
    return HttpResponse('<h1><marquee>Hi Asif</marquee></h1>')
def app4_first(request):
    return HttpResponse('<h1><marquee>Hi LohithRam</marquee></h1>')