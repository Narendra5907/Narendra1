from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app3(request):
    return HttpResponse('<h1>Hi Narendra</h1>')
def app3_first(request):
    return HttpResponse('<h1>Hi vijji</h1>')