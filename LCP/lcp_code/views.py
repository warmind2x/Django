from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homelcp(request):
    return HttpResponse('Hola Mundo desde LCP')