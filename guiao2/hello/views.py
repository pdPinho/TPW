from django.shortcuts import render
from django.http import HttpResponse, HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Hello World!")

def numero(request, num):
    resp = "<html><body><h1>{}</h1></body></html>".format(num);
    return HttpResponse(resp)

